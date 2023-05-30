from scipy.spatial import distance as dist
from collections import OrderedDict


class CentroidTracker:
    def __init__(self, max_disappeared=50):
        self.next_object_id = 0
        self.objects = OrderedDict()
        self.disappeared = OrderedDict()
        self.exit_directions = OrderedDict()
        self.max_disappeared = max_disappeared

    def register(self, centroid, direction):
        self.objects[self.next_object_id] = centroid
        self.disappeared[self.next_object_id] = 0
        self.exit_directions[self.next_object_id] = direction
        self.next_object_id += 1

    def deregister(self, object_id):
        del self.objects[object_id]
        del self.disappeared[object_id]
        del self.exit_directions[object_id]

    def update(self, detections):
        if len(detections) == 0:
            for object_id in list(self.disappeared.keys()):
                self.disappeared[object_id] += 1

                if self.disappeared[object_id] > self.max_disappeared:
                    self.deregister(object_id)

            return self.objects

        input_centroids = [self._get_centroid(detection) for detection in detections]
        if len(self.objects) == 0:
            for i, centroid in enumerate(input_centroids):
                self.register(centroid, 'up')

        else:
            object_ids = list(self.objects.keys())
            object_centroids = list(self.objects.values())

            D = dist.cdist(object_centroids, input_centroids)

            rows = D.min(axis=1).argsort()
            cols = D.argmin(axis=1)[rows]

            used_rows = set()
            used_cols = set()

            for (row, col) in zip(rows, cols):
                if row in used_rows or col in used_cols:
                    continue

                object_id = object_ids[row]
                self.objects[object_id] = input_centroids[col]
                self.disappeared[object_id] = 0

                used_rows.add(row)
                used_cols.add(col)

            unused_rows = set(range(D.shape[0])).difference(used_rows)
            unused_cols = set(range(D.shape[1])).difference(used_cols)

            if D.shape[0] >= D.shape[1]:
                for row in unused_rows:
                    object_id = object_ids[row]
                    self.disappeared[object_id] += 1

                    if self.disappeared[object_id] > self.max_disappeared:
                        self.deregister(object_id)

            else:
                for col in unused_cols:
                    self.register(input_centroids[col], 'down')

        return self.objects

    @staticmethod
    def _get_centroid(detection):
        x, y, w, h = detection
        centroid_x = x + w // 2
        centroid_y = y + h // 2
        return centroid_x, centroid_y
