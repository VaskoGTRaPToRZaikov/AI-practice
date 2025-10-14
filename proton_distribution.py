numbers_of_protons = int(input())

layers_list = []
current_layer = 0

if numbers_of_protons > 0:
    while numbers_of_protons:
        current_layer += 1
        layer_max_protons = current_layer ** 2

        if numbers_of_protons >= layer_max_protons:
            numbers_of_protons -= layer_max_protons
        else:
            layer_max_protons = numbers_of_protons
            numbers_of_protons = 0

        layers_list.append(layer_max_protons)


print(layers_list)