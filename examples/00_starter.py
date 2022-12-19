'''
installation: https://drake.mit.edu/apt.html#stable-releases
ref: https://drake.mit.edu/python_bindings.html#using-the-python-bindings
'''

from pydrake.all import AddMultibodyPlantSceneGraph, DiagramBuilder, FindResourceOrThrow, Parser, Simulator, Adder

def test1():
    builder = DiagramBuilder()
    plant, _ = AddMultibodyPlantSceneGraph(builder, 0.0)
    Parser(plant).AddModels(FindResourceOrThrow("drake/examples/pendulum/Pendulum.urdf"))
    plant.Finalize()
    diagram = builder.Build()
    simulator = Simulator(diagram)

def test2():
    adder = Adder(num_inputs=1, size=1) 
    print(adder)
    print(adder.ToAutoDiffXd())
    print(adder.ToSymbolic()) 

if __name__ == '__main__':
    test2()