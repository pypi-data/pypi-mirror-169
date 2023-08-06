from spotfunctions.v1.executor.executor import Executor
from spotfunctions.v1.executor.configs import AppConfig

if __name__ == "__main__":
    app_config = AppConfig("function.json")
    executor = Executor(app_config)
    executor.run()
