import Pyro4
@Pyro4.expose
class calc:
    def calculate(self, n):
        f = 1
        for i in range(1, n + 1):
            f *= i
        return f

    def mode(self,arr):
        return max(arr,key=arr.count)
daemon=Pyro4.Daemon()
uri=daemon.register(calc)
print("Server URI:", uri, flush=True)
print("Server is running...", flush=True)
daemon.requestLoop()
