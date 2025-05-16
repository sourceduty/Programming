import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def layer_animation(layers_data, frames, interval=200, repeat=True, axes=None, save_path=None, **kwargs):
    """
    Animate multiple plots or graphical elements over time on a single figure.
    """
    # Create figure and axes if not provided
    if axes is None:
        fig, ax = plt.subplots()
        axes = ax  # Assign to axes for consistency
    else:
        fig = axes.figure

    # Initialize an empty list to store plot objects
    plots = []

    # Setup each layer and add initial plots
    for layer in layers_data:
        plot_type = layer.get("type")
        initial_data = layer.get("data")[0]  # Use the first frame data
        plot_kwargs = layer.get("kwargs", {})
        plot_kwargs.update(kwargs)

        if plot_type == "line":
            plot, = axes.plot(initial_data["x"], initial_data["y"], **plot_kwargs)
        elif plot_type == "scatter":
            plot = axes.scatter(initial_data["x"], initial_data["y"], **plot_kwargs)
        elif plot_type == "bar":
            plot = axes.bar(initial_data["x"], initial_data["y"], **plot_kwargs)
        # Additional plot types can be added here

        plots.append(plot)

    def update(frame):
        """Update function for the animation."""
        for i, layer in enumerate(layers_data):
            data = layer.get("data")[frame]
            plot_type = layer.get("type")

            if plot_type == "line":
                plots[i].set_data(data["x"], data["y"])
            elif plot_type == "scatter":
                plots[i].set_offsets(list(zip(data["x"], data["y"])))
            elif plot_type == "bar":
                for rect, y in zip(plots[i], data["y"]):
                    rect.set_height(y)
            # Add updates for additional plot types if necessary

        return plots

    # Create animation
    anim = FuncAnimation(fig, update, frames=frames, interval=interval, repeat=repeat)

    # Save animation if save_path is provided
    if save_path:
        anim.save(save_path, writer='imagemagick' if save_path.endswith('.gif') else 'ffmpeg')

    return anim

# Example usage
layers_data = [
    {"type": "line", "data": [{"x": [1, 2, 3], "y": [4, 5, 6]}, {"x": [1, 2, 3], "y": [6, 5, 4]}], "kwargs": {"color": "blue", "label": "Line Plot"}},
    {"type": "scatter", "data": [{"x": [1, 2, 3], "y": [6, 5, 4]}, {"x": [1, 2, 3], "y": [5, 6, 7]}], "kwargs": {"color": "red", "label": "Scatter Plot"}},
]

# Create an animation with 2 frames
anim = layer_animation(layers_data, frames=2, interval=500, repeat=True)

# Display the animation
plt.show()
