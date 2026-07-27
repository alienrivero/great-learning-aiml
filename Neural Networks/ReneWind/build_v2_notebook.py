import copy
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "INN_ReneWind_Main_Project_FullCode_Notebook.ipynb"
TARGET = HERE / "INN_ReneWind_Main_Project_FullCode_Notebook_V2.ipynb"


def md(text):
    return {"cell_type": "markdown", "metadata": {}, "source": text.splitlines(keepends=True)}


def code(text):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": text.splitlines(keepends=True),
    }


nb = json.loads(SOURCE.read_text(encoding="utf-8"))
cells = copy.deepcopy(nb["cells"][:25])

# Update the dependency cell while retaining the course notebook's familiar setup.
cells[8]["source"] = (
    "# Install once if these packages are not already available.\n"
    "# After installation, restart the kernel and continue from the next cell.\n"
    "!pip install tensorflow==2.19.0 keras-tuner==1.4.8 tensorboard scikit-learn==1.6.1 "
    "matplotlib==3.10.0 seaborn==0.13.2 numpy==2.0.2 pandas==2.2.2 -q\n"
).splitlines(keepends=True)

# Extend imports in the original loading cell.
src = "".join(cells[11]["source"])
src = src.replace("import tensorflow as tf", "import tensorflow as tf\nimport keras_tuner as kt")
src = src.replace("    f1_score,\n", "    f1_score,\n    average_precision_score,\n")
cells[11]["source"] = src.splitlines(keepends=True)

cells.extend([
md("""# **Model Building and Hyperparameter Tuning (V2)**

## Experimental design and feedback on the proposed six-model plan

The original idea is directionally strong because it demonstrates the six improvement combinations required by the rubric. The following refinements make the comparison more defensible:

- **Keep Model 0 as a fixed baseline.** It provides an honest reference and is not tuned.
- **Tune model families, not a single ever-growing network.** Each family answers a clear question: class weights, optimizer, dropout, batch normalization, and regularization.
- **Use validation PR-AUC as the tuning objective.** Recall is the business priority, but optimizing recall alone can reward a model that predicts nearly every turbine as a failure. PR-AUC is more informative than accuracy or ROC-AUC for a 5.5% positive class.
- **Tune the decision threshold separately on validation data.** The default 0.50 threshold is rarely optimal when class weights are used. We choose the highest-F1 threshold that achieves at least 90% validation recall, then lock it before the one-time test evaluation.
- **Use only course-demonstrated activation/initialization choices.** The shared neural-network notebooks explicitly use ReLU and tanh in hidden layers, and demonstrate `he_normal` / `he_uniform` kernel initialization. Those are the only choices searched. Bias initialization is left at Keras' standard zero default rather than introducing an unseen technique.
- **Momentum belongs to SGD, not Adam.** Model 6 therefore uses regularized SGD with tuned momentum. Adam already maintains adaptive first/second moment estimates and has no Keras `momentum` argument.

The test set remains untouched throughout architecture, hyperparameter, model, and threshold selection.
"""),
md("""## Model evaluation criterion

A false negative means a real generator failure is missed and may require full replacement, the costliest outcome. Therefore **failure-class recall is the primary operational constraint**. Precision and F1 are also reported so the model does not create an impractical inspection burden. During tuning, **validation PR-AUC** is optimized; during model selection, candidates satisfying at least 90% validation recall are ranked by validation F1.
"""),
code("""# Reproducibility and shared evaluation utilities
SEED = 42
tf.keras.utils.set_random_seed(SEED)
try:
    tf.config.experimental.enable_op_determinism()
except Exception:
    pass

MIN_RECALL = 0.90
MAX_EPOCHS = 60
MAX_TRIALS = 8       # Increase to 12-20 if more compute time is available
EXECUTIONS_PER_TRIAL = 1

def keras_metrics():
    return [
        tf.keras.metrics.Recall(name="recall"),
        tf.keras.metrics.Precision(name="precision"),
        tf.keras.metrics.AUC(curve="PR", name="pr_auc"),
        tf.keras.metrics.BinaryAccuracy(name="accuracy"),
    ]

def make_optimizer(name, learning_rate, momentum=0.0):
    if name == "sgd":
        return SGD(learning_rate=learning_rate, momentum=momentum)
    return Adam(learning_rate=learning_rate)

def make_regularizer(l1=0.0, l2=0.0):
    if l1 == 0 and l2 == 0:
        return None
    return tf.keras.regularizers.L1L2(l1=l1, l2=l2)

def build_network(input_dim, units, activation="relu", kernel_initializer="he_normal",
                  optimizer_name="adam", learning_rate=1e-3, dropout_rate=0.0,
                  use_batch_norm=False, l1=0.0, l2=0.0, momentum=0.0):
    model = Sequential(name="renwind_ann")
    model.add(tf.keras.Input(shape=(input_dim,)))
    reg = make_regularizer(l1, l2)
    for width in units:
        model.add(Dense(width, activation=activation,
                        kernel_initializer=kernel_initializer,
                        bias_initializer="zeros", kernel_regularizer=reg))
        if use_batch_norm:
            model.add(BatchNormalization())
        if dropout_rate > 0:
            model.add(Dropout(dropout_rate))
    model.add(Dense(1, activation="sigmoid", bias_initializer="zeros"))
    model.compile(
        optimizer=make_optimizer(optimizer_name, learning_rate, momentum),
        loss="binary_crossentropy",
        metrics=keras_metrics(),
    )
    return model

def probabilities(model, X):
    return model.predict(X, verbose=0).ravel()

def metric_row(y_true, prob, threshold=0.50):
    pred = (prob >= threshold).astype(int)
    return {
        "Threshold": threshold,
        "Recall": recall_score(y_true, pred),
        "Precision": precision_score(y_true, pred, zero_division=0),
        "F1": f1_score(y_true, pred, zero_division=0),
        "Accuracy": accuracy_score(y_true, pred),
        "PR AUC": average_precision_score(y_true, prob),
    }

def choose_threshold(y_true, prob, min_recall=MIN_RECALL):
    rows = [metric_row(y_true, prob, t) for t in np.linspace(0.05, 0.95, 181)]
    table = pd.DataFrame(rows)
    feasible = table[table["Recall"] >= min_recall]
    selected = (feasible.sort_values(["F1", "Precision"], ascending=False).iloc[0]
                if len(feasible) else table.sort_values(["Recall", "F1"], ascending=False).iloc[0])
    return float(selected["Threshold"]), table

def plot_history(history, title):
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    axes[0].plot(history.history["loss"], label="Train")
    axes[0].plot(history.history["val_loss"], label="Validation")
    axes[0].set_title(f"{title}: Loss")
    axes[1].plot(history.history["pr_auc"], label="Train")
    axes[1].plot(history.history["val_pr_auc"], label="Validation")
    axes[1].set_title(f"{title}: PR-AUC")
    for ax in axes:
        ax.set_xlabel("Epoch")
        ax.legend()
    plt.tight_layout()
    plt.show()

experiment_results = {}
trained_models = {}
histories = {}
threshold_tables = {}
"""),
md("""## Model 0 — Untuned baseline

One hidden layer, ReLU, SGD, and no class weights. This intentionally simple model establishes the baseline required by the rubric.
"""),
code("""tf.keras.backend.clear_session()
tf.keras.utils.set_random_seed(SEED)
model_0 = build_network(
    X_train_scaled.shape[1], units=[32], activation="relu",
    kernel_initializer="he_normal", optimizer_name="sgd", learning_rate=0.01
)
history_0 = model_0.fit(
    X_train_scaled, y_train, validation_data=(X_val_scaled, y_val),
    epochs=MAX_EPOCHS, batch_size=32, verbose=0,
    callbacks=[EarlyStopping(monitor="val_pr_auc", mode="max", patience=8,
                             restore_best_weights=True)]
)
prob_0 = probabilities(model_0, X_val_scaled)
threshold_0, threshold_tables["Model 0"] = choose_threshold(y_val, prob_0)
experiment_results["Model 0: Baseline SGD"] = metric_row(y_val, prob_0, 0.50)
trained_models["Model 0: Baseline SGD"] = model_0
histories["Model 0: Baseline SGD"] = history_0
plot_history(history_0, "Model 0")
pd.DataFrame([experiment_results["Model 0: Baseline SGD"]])
"""),
md("""## Keras Tuner infrastructure

`ReneWindHyperModel` tunes architecture and training hyperparameters. Conditional search spaces ensure each model family changes only the techniques under study. Batch size and early-stopping patience are valid training hyperparameters, so they are tuned in `fit()` rather than in `build()`.
"""),
code("""class ReneWindHyperModel(kt.HyperModel):
    def __init__(self, optimizer_name, allow_dropout=False, use_batch_norm=False,
                 allow_regularization=False, tune_momentum=False):
        self.optimizer_name = optimizer_name
        self.allow_dropout = allow_dropout
        self.use_batch_norm = use_batch_norm
        self.allow_regularization = allow_regularization
        self.tune_momentum = tune_momentum

    def build(self, hp):
        n_layers = hp.Int("n_layers", 1, 4)
        units = [hp.Choice(f"units_{i}", [16, 32, 64, 128]) for i in range(n_layers)]
        # Restricted to techniques explicitly demonstrated in the supplied course notebooks.
        activation = hp.Choice("activation", ["relu", "tanh"])
        initializer = hp.Choice("kernel_initializer", ["he_normal", "he_uniform"])
        learning_rate = hp.Choice(
            "learning_rate",
            [1e-4, 3e-4, 1e-3, 3e-3] if self.optimizer_name == "adam"
            else [1e-3, 3e-3, 1e-2, 3e-2]
        )
        dropout = hp.Choice("dropout_rate", [0.10, 0.20, 0.30, 0.40]) if self.allow_dropout else 0.0
        l1 = hp.Choice("l1", [0.0, 1e-6, 1e-5, 1e-4]) if self.allow_regularization else 0.0
        l2 = hp.Choice("l2", [0.0, 1e-5, 1e-4, 1e-3]) if self.allow_regularization else 0.0
        momentum = hp.Choice("momentum", [0.0, 0.5, 0.9]) if self.tune_momentum else 0.0
        return build_network(
            X_train_scaled.shape[1], units, activation, initializer,
            self.optimizer_name, learning_rate, dropout, self.use_batch_norm,
            l1, l2, momentum
        )

    def fit(self, hp, model, *args, **kwargs):
        kwargs["batch_size"] = hp.Choice("batch_size", [32, 64, 128])
        patience = hp.Choice("patience", [5, 8, 12])
        callbacks = list(kwargs.pop("callbacks", []))
        callbacks.append(EarlyStopping(
            monitor="val_pr_auc", mode="max", patience=patience,
            restore_best_weights=True
        ))
        return model.fit(*args, callbacks=callbacks, **kwargs)

def tune_family(label, hypermodel):
    tf.keras.backend.clear_session()
    tf.keras.utils.set_random_seed(SEED)
    tuner = kt.RandomSearch(
        hypermodel,
        objective=kt.Objective("val_pr_auc", direction="max"),
        max_trials=MAX_TRIALS,
        executions_per_trial=EXECUTIONS_PER_TRIAL,
        seed=SEED,
        overwrite=True,
        directory="keras_tuner_results",
        project_name=("model_" + "".join(
            ch if ch.isalnum() else "_" for ch in label.lower()
        )).strip("_"),
    )
    tuner.search(
        X_train_scaled, y_train,
        validation_data=(X_val_scaled, y_val),
        class_weight=class_weight_dict,
        epochs=MAX_EPOCHS,
        verbose=0,
    )
    best_hp = tuner.get_best_hyperparameters(1)[0]
    model = tuner.hypermodel.build(best_hp)
    history = tuner.hypermodel.fit(
        best_hp, model, X_train_scaled, y_train,
        validation_data=(X_val_scaled, y_val),
        class_weight=class_weight_dict,
        epochs=MAX_EPOCHS,
        verbose=0,
    )
    prob = probabilities(model, X_val_scaled)
    threshold, threshold_table = choose_threshold(y_val, prob)
    result = metric_row(y_val, prob, threshold)
    result["Default 0.50 Recall"] = metric_row(y_val, prob, 0.50)["Recall"]
    result["Default 0.50 F1"] = metric_row(y_val, prob, 0.50)["F1"]
    experiment_results[label] = result
    trained_models[label] = model
    histories[label] = history
    threshold_tables[label] = threshold_table
    print(label)
    print("Best hyperparameters:", best_hp.values)
    print("Selected validation threshold:", round(threshold, 3))
    display(pd.DataFrame([result]))
    plot_history(history, label)
    return tuner, best_hp
"""),
md("""## Model 1 — Tuned SGD + class weights

This isolates the effect of class weighting while allowing Keras Tuner to select depth, width, activation, initializer, learning rate, batch size, and patience.
"""),
code("""tuner_1, hp_1 = tune_family(
    "Model 1: Tuned SGD + Class Weights",
    ReneWindHyperModel(optimizer_name="sgd")
)
"""),
md("""## Model 2 — Tuned Adam + class weights

This model uses the same search dimensions as Model 1 but changes the optimizer to Adam, making the optimizer comparison fair.
"""),
code("""tuner_2, hp_2 = tune_family(
    "Model 2: Tuned Adam + Class Weights",
    ReneWindHyperModel(optimizer_name="adam")
)
"""),
md("""## Model 3 — Tuned Adam + dropout + class weights

Dropout is added as a tunable regularizer. Rates are deliberately constrained to 0.10–0.40; extreme dropout would be unlikely to help a small tabular network.
"""),
code("""tuner_3, hp_3 = tune_family(
    "Model 3: Tuned Adam + Dropout + Class Weights",
    ReneWindHyperModel(optimizer_name="adam", allow_dropout=True)
)
"""),
md("""## Model 4 — Tuned Adam + dropout + batch normalization + class weights

To remain consistent with the supplied course notebook, activation is applied inside each `Dense` layer, followed by Batch Normalization and then Dropout: `Dense + activation → BatchNormalization → Dropout`.
"""),
code("""tuner_4, hp_4 = tune_family(
    "Model 4: Tuned Adam + Dropout + BatchNorm + Class Weights",
    ReneWindHyperModel(optimizer_name="adam", allow_dropout=True, use_batch_norm=True)
)
"""),
md("""## Model 5 — Tuned Adam + dropout + batch normalization + L1/L2 + class weights

This is the most heavily regularized Adam family. L1 and L2 strengths are tuned independently, including zero, so the search can reject unnecessary regularization.
"""),
code("""tuner_5, hp_5 = tune_family(
    "Model 5: Tuned Adam + Dropout + BatchNorm + L1/L2 + Class Weights",
    ReneWindHyperModel(
        optimizer_name="adam", allow_dropout=True,
        use_batch_norm=True, allow_regularization=True
    )
)
"""),
md("""## Model 6 — Tuned SGD momentum + dropout + batch normalization + L1/L2 + class weights

Momentum is evaluated where it is technically meaningful: with SGD. This final family tests whether classical momentum plus the full regularization stack can outperform the Adam families.
"""),
code("""tuner_6, hp_6 = tune_family(
    "Model 6: Tuned SGD Momentum + Dropout + BatchNorm + L1/L2 + Class Weights",
    ReneWindHyperModel(
        optimizer_name="sgd", allow_dropout=True, use_batch_norm=True,
        allow_regularization=True, tune_momentum=True
    )
)
"""),
md("""# **Model comparison and final selection**

The table uses each tuned model's validation-selected threshold. Models meeting the 90% recall constraint are ranked by F1, then PR-AUC. This is more business-aligned than selecting the largest raw recall and more robust than selecting on accuracy.
"""),
code("""comparison_df = (
    pd.DataFrame(experiment_results).T
    .sort_values(["F1", "PR AUC"], ascending=False)
)
display(comparison_df.style.format("{:.4f}"))

eligible = comparison_df[comparison_df["Recall"] >= MIN_RECALL]
if len(eligible):
    best_model_name = eligible.sort_values(["F1", "PR AUC"], ascending=False).index[0]
else:
    best_model_name = comparison_df.sort_values(["Recall", "F1"], ascending=False).index[0]

best_model = trained_models[best_model_name]
best_threshold = float(comparison_df.loc[best_model_name, "Threshold"])
print("Selected model:", best_model_name)
print("Locked threshold:", round(best_threshold, 3))
"""),
code("""# Visual comparison
plot_cols = ["Recall", "Precision", "F1", "PR AUC"]
comparison_df[plot_cols].sort_values("F1").plot(
    kind="barh", figsize=(11, 7), xlim=(0, 1), title="Validation performance by model"
)
plt.xlabel("Score")
plt.tight_layout()
plt.show()
"""),
md("""## One-time final evaluation on the untouched test set

Only the selected model and its locked validation threshold are now applied to `Test.csv`. No decisions are revised after viewing these results.
"""),
code("""test_prob = probabilities(best_model, X_test_scaled)
test_metrics = metric_row(y_test, test_prob, best_threshold)
display(pd.DataFrame([test_metrics], index=[best_model_name]).style.format("{:.4f}"))

test_pred = (test_prob >= best_threshold).astype(int)
cm = confusion_matrix(y_test, test_pred)
plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Final Model — Test Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
print(classification_report(y_test, test_pred, digits=4))
"""),
md("""# **Actionable insights and recommendations**

- **Use the selected tuned network as a screening model**, sending predicted failures for inspection before breakdown. Report both recall and the number of false alarms to maintenance planners.
- **Treat the probability threshold as an operational control.** The notebook locks a validation-selected threshold that targets at least 90% recall. Once actual inspection, repair, and replacement costs are available, replace the F1 rule with direct expected-cost minimization.
- **Do not assume the most complex network is best.** The controlled model-family comparison shows whether dropout, batch normalization, L1/L2, and momentum add measurable validation value rather than awarding complexity for its own sake.
- **Collect more failure cases.** Only about 5.5% of records are failures, so additional confirmed failures will reduce dependence on large class weights and improve estimates of rare-event performance.
- **Monitor data and recall drift.** Sensor distributions and turbine wear can change. Track input drift, failure-class recall, false alarms per inspection cycle, and recalibrate/retrain on a defined schedule.
- **Connect anonymized variables to engineering systems.** The strongest target-associated features should be mapped back to sensor/subsystem names with domain experts so alerts can guide the correct inspection procedure.

## Final submission checklist

1. Run all cells from a fresh kernel and confirm there are no errors.
2. Add one or two model-specific observations beneath each tuner result after execution.
3. Confirm the final test set is evaluated only once.
4. Export the fully executed notebook to HTML for submission.
"""),
])

nb["cells"] = cells
nb["metadata"].setdefault("kernelspec", {"display_name": "Python 3", "language": "python", "name": "python3"})
TARGET.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
print(TARGET)
