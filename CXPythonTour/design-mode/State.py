# coding=utf-8

"""
Created on 2017-11-29
@author: Palesnow

功能：状态模式
网址：https://yq.aliyun.com/articles/71198

实例：电梯控制器

"""

# 抽象状态类
class LiftState:
    def open(self):
        pass
    def close(self):
        pass
    def run(self):
        pass
    def stop(self):
        pass
# 具体的状态类
class OpenState(LiftState):
    def open(self):
        print("OPEN: The door is opened")
        return self
    def close(self):
        print("OPEN: The door start to close")
        print("OPEN: The door is closed")
        return StopState()
    def run(self):
        print("OPEN: Run Forbidden")
        return self
    def stop(self):
        print("OPEN: Stop Forbidden")
        return self
class RunState(LiftState):
    def open(self):
        print("RUN: Open Forbidden.")
        return self
    def close(self):
        print("RUN: Close Forbidden.")
        return self
    def run(self):
        print("RUN: The lift is running")
        return self
    def stop(self):
        print("RUN: The lift start to stop")
        print("RUN: The lift is stopped")
        return StopState()
class StopState(LiftState):
    def open(self):
        print("STOP: The door is opening")
        print("STOP: The door is opened")
        return OpenState()
    def close(self):
        print("STOP: Close Forbidden")
        return self
    def run(self):
        print("STOP: The lift start to run")
        return RunState()
    def stop(self):
        print("STOP: The lift is stopped")
        return self

class Context:
    lift_state = ""
    def getState(self):
        return self.lift_state
    def setState(self, lift_state):
        self.lift_state = lift_state
    def open(self):
        self.setState(self.lift_state.open())
    def close(self):
        self.setState(self.lift_state.close())
    def run(self):
        self.setState(self.lift_state.run())
    def stop(self):
        self.setState(self.lift_state.stop())

if __name__ == "__main__":
    ctx = Context()
    print("=====开门-》运行-》停止======")
    ctx.setState(StopState())
    ctx.open()
    ctx.close()
    ctx.run()
    ctx.stop()
    print("=====开门-》关门-》停止======")
    ctx.open()
    ctx.close()
    ctx.stop()

