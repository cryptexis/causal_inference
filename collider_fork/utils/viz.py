from graphviz import Digraph


def create_graph(scm, shade_nodes=()):

    dot = Digraph(comment=scm.name)

    for eq in scm.equations:
        if eq['output_variable'].name in shade_nodes:
            dot.node(eq['output_variable'].name, style='filled', color='lightgrey')
        else:
            dot.node(eq['output_variable'].name)

        input_vars = list(map(lambda n: n.name, eq['input_variables'].keys()))
        for input_var in input_vars:
            dot.edge(input_var, eq['output_variable'].name, constraint='true')

    return dot
