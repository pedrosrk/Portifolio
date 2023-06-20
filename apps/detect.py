import cv2, os

class ObjDetect:
    def __init__(self, image):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        parent_directory = os.path.dirname(current_dir)
        img = cv2.imread(os.path.join(parent_directory, 'static', 'assets', image))
        self.picture = img
    
    def get_picture(self):
        return self.picture
    
    def set_picture(self, new_image):
        self.picture = cv2.imread(new_image)

    def save_detect_picture(self):
        image = cv2.resize(self.picture, (640, 480))
        h = image.shape[0]
        w = image.shape[1]

        current_dir = os.path.dirname(os.path.realpath(__file__))
        parent_directory = os.path.dirname(current_dir)
        
        #weights = "static/assets/frozen_inference_graph.pb"
        weights = os.path.join(parent_directory, 'static', 'assets', 'frozen_inference_graph.pb')
        #model = "static/assets/large_coco_2020_01_14.pbtxt"
        model = os.path.join(parent_directory, 'static', 'assets', 'large_coco_2020_01_14.pbtxt')

        net = cv2.dnn.readNetFromTensorflow(weights, model)

        class_names = []
        #with open("static/assets/coco_names.txt", "r") as f:
        with open(os.path.join(parent_directory, 'static', 'assets','coco_names.txt'), "r") as f:
            class_names = f.read().strip().split("\n")

        blob = cv2.dnn.blobFromImage(
            image, 1.0/127.5, (320, 320), [127.5, 127.5, 127.5])

        net.setInput(blob)
        output = net.forward()  

        for detection in output[0, 0, :, :]:  
            probability = detection[2]
            if probability < 0.5:
                continue
            box = [int(a * b) for a, b in zip(detection[3:7], [w, h, w, h])]
            box = tuple(box)
            cv2.rectangle(image, box[:2], box[2:], (0, 255, 0), thickness=2)
            class_id = int(detection[1])
            label = f"{class_names[class_id - 1].upper()} {probability * 100:.2f}%"
            cv2.putText(image, label, (box[0], box[1] + 15),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        #cv2.imwrite('static/assets/output.jpg', image)
        cv2.imwrite(os.path.join(parent_directory, 'static', 'assets', 'output.jpg'), image)

    def __str__(self):
        image = cv2.resize(self.picture, (640, 480))
        h = image.shape[0]
        w = image.shape[1]

        current_dir = os.path.dirname(os.path.realpath(__file__))
        parent_directory = os.path.dirname(current_dir)

        #weights = "static/assets/frozen_inference_graph.pb"
        weights = os.path.join(parent_directory, 'static', 'assets', 'frozen_inference_graph.pb')
        #model = "static/assets/large_coco_2020_01_14.pbtxt"
        model = os.path.join(parent_directory, 'static', 'assets', 'large_coco_2020_01_14.pbtxt')

        net = cv2.dnn.readNetFromTensorflow(weights, model)

        class_names = []
        #with open("static/assets/coco_names.txt", "r") as f:
        with open(os.path.join(parent_directory, 'static', 'assets','coco_names.txt'), "r") as f:
            class_names = f.read().strip().split("\n")

        blob = cv2.dnn.blobFromImage(
            image, 1.0/127.5, (320, 320), [127.5, 127.5, 127.5])

        net.setInput(blob)
        output = net.forward()  

        for detection in output[0, 0, :, :]:  
            probability = detection[2]
            if probability < 0.5:
                continue
            box = [int(a * b) for a, b in zip(detection[3:7], [w, h, w, h])]
            box = tuple(box)
            cv2.rectangle(image, box[:2], box[2:], (0, 255, 0), thickness=2)
            class_id = int(detection[1])
            label = f"{class_names[class_id - 1].upper()} {probability * 100:.2f}%"
            cv2.putText(image, label, (box[0], box[1] + 15),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow('Image', image)
        cv2.waitKey()
