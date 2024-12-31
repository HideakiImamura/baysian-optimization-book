import optuna

from sampler import GPUCBSampler

def objective(trial: optuna.Trial) -> float:
    x = trial.suggest_float("x", -10, 10)
    return x ** 2


if __name__ == "__main__":
    study = optuna.create_study(
        sampler=GPUCBSampler(),
    )
    study.optimize(objective, n_trials=100)
    print(study.best_params)
    print(study.best_value)