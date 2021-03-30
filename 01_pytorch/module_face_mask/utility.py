import matplotlib.pyplot as plt
import matplotlib.patches as patches
        
def do_plot(image, annotation):
    fig, ax = plt.subplots(1)
    ax.imshow(image)

    boxes = annotation['boxes']
    labels = annotation['labels']
    for box, label in zip(boxes, labels):
        xmin, ymin, xmax, ymax = box
        if label == 0:
            rect = patches.Rectangle((xmin, ymin), (xmax-xmin), (ymax-ymin), linewidth=3, edgecolor='r', facecolor='none')
        elif label == 1:
            rect = patches.Rectangle((xmin, ymin), (xmax-xmin), (ymax-ymin), linewidth=3, edgecolor='g', facecolor='none')
        elif label == 2:
            rect = patches.Rectangle((xmin, ymin), (xmax-xmin), (ymax-ymin), linewidth=3, edgecolor='y', facecolor='none')
        ax.add_patch(rect)
    plt.show()