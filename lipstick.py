import cv2
import dlib
import numpy as np

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("C://Users/omkar/Downloads/shape_predictor_68_face_landmarks.dat")
predictor2 = dlib.shape_predictor("E://shape_predictor_194_face_landmarks.dat")


# rgb(220,20,60)

def lipstick(frame,red,blue,green,red1,blue1,green1,pigment=0.3,pigment1=0.7):
        fr = frame
        fr = cv2.flip(fr,1)
        output = fr.copy()
        output2 = fr.copy()
        gray_fr = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
        # faces = facec.detectMultiScale(gray_fr, 1.3, 5)
        faces2 = detector(gray_fr)

        def l(i):
            return (landmarks.part(i).x,landmarks.part(i).y)

        def li(i):
            return (landmarks2.part(i).x,landmarks2.part(i).y)

        for face in faces2:

            landmarks = predictor(gray_fr, face)
            landmarks2 = predictor2(gray_fr, face)
            
            for n in range(0, 68):
                pts_array = np.array([l(54),l(55),l(56),l(57),l(58),l(59),l(48),l(60),l(67),l(66),l(65),l(64)],np.int32)
                pts_array = pts_array.reshape((-1,1,2))
                cv2.fillPoly(fr,[pts_array],(blue,green,red))
                pts_array2 = np.array([l(48),l(49),l(50),l(51),l(52),l(53),l(54),l(64),l(63),l(62),l(61),l(60)],np.int32)
                pts_array2 = pts_array2.reshape((-1,1,2))
                cv2.fillPoly(fr,[pts_array2],(blue,green,red))
                dist_x = li(37)[0] - li(33)[0]
                dist_x = int(dist_x)
                newPt = (li(37)[0]+dist_x,li(33)[1])
                pts_array3 = np.array([newPt,li(33),li(37)])
                pts_array3 = pts_array3.reshape((-1,1,2))
                cv2.fillPoly(output2,[pts_array3],(blue1,green1,red1))
                cv2.line(output2, li(27), li(28), (blue1,green1,red1), 1)
                cv2.line(output2, li(28), li(29), (blue1,green1,red1), 1)
                cv2.line(output2, li(29), li(30), (blue1,green1,red1), 1)
                cv2.line(output2, li(30), li(31), (blue1,green1,red1), 2)
                cv2.line(output2, li(31), li(33), (blue1,green1,red1), 2)
                cv2.line(output2, li(33), li(34), (blue1,green1,red1), 2)
                cv2.line(output2, li(34), li(35), (blue1,green1,red1), 2)
                cv2.line(output2, li(35), li(36), (blue1,green1,red1), 2)
                cv2.line(output2, li(36), li(37), (blue1,green1,red1), 3)

                dist_x2 = li(59)[0] - li(55)[0]
                dist_x2 = int(dist_x2)
                newPt2 = (li(59)[0]+dist_x2,li(55)[1])
                pts_array4 = np.array([newPt2,li(55),li(59)])
                pts_array4 = pts_array4.reshape((-1,1,2))
                cv2.fillPoly(output2,[pts_array4],(blue1,green1,red1))
                cv2.line(output2, li(59), li(58), (blue1,green1,red1), 3)
                cv2.line(output2, li(58), li(57), (blue1,green1,red1), 3)
                cv2.line(output2, li(57), li(56), (blue1,green1,red1), 2)
                cv2.line(output2, li(56), li(55), (blue1,green1,red1), 2)
                cv2.line(output2, li(55), li(53), (blue1,green1,red1), 2)
                cv2.line(output2, li(53), li(52), (blue1,green1,red1), 1)
                cv2.line(output2, li(52), li(51), (blue1,green1,red1), 1)
                cv2.line(output2, li(51), li(50), (blue1,green1,red1), 1)
                cv2.line(output2, li(50), li(49), (blue1,green1,red1), 1)

        cv2.addWeighted(output2, 0.7, output, 1 - 0.7,0, output)
        cv2.addWeighted(fr, pigment, output, 1 - 0.3,0, output)
        
        return output