def main():
    """Main function."""
    with open('day_8.input') as input_file:
        input_data = input_file.readline().strip()
        layers = []
        size = len(input_data)
        width = 25
        height = 6
        layer = 0
        while size >= (layer * width * height) + (width * height):
            layers.append([int(x) for x in input_data[(layer * width * height):((layer + 1) * width * height)]])
            layer += 1

        layer_data = {}
        for i, layer in enumerate(layers):
            layer_data[i] = {0: layer.count(0), 1: layer.count(1), 2: layer.count(2)}
        sorted_layer_data = sorted(layer_data.items(), key=lambda x: x[1][0])

        print(sorted_layer_data[0][1][1] * sorted_layer_data[0][1][2])

        resulting_image = list(layers[len(layers) - 1])
        for layer in reversed(layers):
            for i, pixel in enumerate(layer):
                if pixel != 2:
                    resulting_image[i] = pixel

        # improve visibility
        resulting_image = "".join(['█' if x == 1 else ' ' for x in resulting_image])

        # Print image
        for row in range(height):
            print(resulting_image[row * width: (row + 1) * width])


if __name__ == '__main__':
    main()
