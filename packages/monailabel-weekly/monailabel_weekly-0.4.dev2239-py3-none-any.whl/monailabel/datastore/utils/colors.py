# Copyright (c) MONAI Consortium
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

GENERIC_ANATOMY_COLORS = {
    "background": (0, 0, 0),
    "tissue": (128, 174, 128),
    "bone": (241, 214, 145),
    "skin": (177, 122, 101),
    "connective tissue": (111, 184, 210),
    "blood": (216, 101, 79),
    "organ": (221, 130, 101),
    "mass": (144, 238, 144),
    "muscle": (192, 104, 88),
    "foreign object": (220, 245, 20),
    "waste": (78, 63, 0),
    "teeth": (255, 250, 220),
    "fat": (230, 220, 70),
    "gray matter": (200, 200, 235),
    "white matter": (250, 250, 210),
    "nerve": (244, 214, 49),
    "vein": (0, 151, 206),
    "artery": (216, 101, 79),
    "capillary": (183, 156, 220),
    "ligament": (183, 214, 211),
    "tendon": (152, 189, 207),
    "cartilage": (111, 184, 210),
    "meniscus": (178, 212, 242),
    "lymph node": (68, 172, 100),
    "lymphatic vessel": (111, 197, 131),
    "cerebro-spinal fluid": (85, 188, 255),
    "bile": (0, 145, 30),
    "urine": (214, 230, 130),
    "feces": (78, 63, 0),
    "gas": (218, 255, 255),
    "fluid": (170, 250, 250),
    "edema": (140, 224, 228),
    "bleeding": (188, 65, 28),
    "necrosis": (216, 191, 216),
    "clot": (145, 60, 66),
    "embolism": (150, 98, 83),
    "head": (177, 122, 101),
    "central nervous system": (244, 214, 49),
    "brain": (250, 250, 225),
    "gray matter of brain": (200, 200, 215),
    "telencephalon": (68, 131, 98),
    "cerebral cortex": (128, 174, 128),
    "right frontal lobe": (83, 146, 164),
    "left frontal lobe": (83, 146, 164),
    "right temporal lobe": (162, 115, 105),
    "left temporal lobe": (162, 115, 105),
    "right parietal lobe": (141, 93, 137),
    "left parietal lobe": (141, 93, 137),
    "right occipital lobe": (182, 166, 110),
    "left occipital lobe": (182, 166, 110),
    "right insular lobe": (188, 135, 166),
    "left insular lobe": (188, 135, 166),
    "right limbic lobe": (154, 150, 201),
    "left limbic lobe": (154, 150, 201),
    "right striatum": (177, 140, 190),
    "left striatum": (177, 140, 190),
    "right caudate nucleus": (30, 111, 85),
    "left caudate nucleus": (30, 111, 85),
    "right putamen": (210, 157, 166),
    "left putamen": (210, 157, 166),
    "right pallidum": (48, 129, 126),
    "left pallidum": (48, 129, 126),
    "right amygdaloid complex": (98, 153, 112),
    "left amygdaloid complex": (98, 153, 112),
    "diencephalon": (69, 110, 53),
    "thalamus": (166, 113, 137),
    "right thalamus": (122, 101, 38),
    "left thalamus": (122, 101, 38),
    "pineal gland": (253, 135, 192),
    "midbrain": (145, 92, 109),
    "substantia nigra": (46, 101, 131),
    "right substantia nigra": (0, 108, 112),
    "left substantia nigra": (0, 108, 112),
    "cerebral white matter": (250, 250, 225),
    "right superior longitudinal fasciculus": (127, 150, 88),
    "left superior longitudinal fasciculus": (127, 150, 88),
    "right inferior longitudinal fasciculus": (159, 116, 163),
    "left inferior longitudinal fasciculus": (159, 116, 163),
    "right arcuate fasciculus": (125, 102, 154),
    "left arcuate fasciculus": (125, 102, 154),
    "right uncinate fasciculus": (106, 174, 155),
    "left uncinate fasciculus": (106, 174, 155),
    "right cingulum bundle": (154, 146, 83),
    "left cingulum bundle": (154, 146, 83),
    "projection fibers": (126, 126, 55),
    "right corticospinal tract": (201, 160, 133),
    "left corticospinal tract": (201, 160, 133),
    "right optic radiation": (78, 152, 141),
    "left optic radiation": (78, 152, 141),
    "right medial lemniscus": (174, 140, 103),
    "left medial lemniscus": (174, 140, 103),
    "right superior cerebellar peduncle": (139, 126, 177),
    "left superior cerebellar peduncle": (139, 126, 177),
    "right middle cerebellar peduncle": (148, 120, 72),
    "left middle cerebellar peduncle": (148, 120, 72),
    "right inferior cerebellar peduncle": (186, 135, 135),
    "left inferior cerebellar peduncle": (186, 135, 135),
    "optic chiasm": (99, 106, 24),
    "right optic tract": (156, 171, 108),
    "left optic tract": (156, 171, 108),
    "right fornix": (64, 123, 147),
    "left fornix": (64, 123, 147),
    "commissural fibers": (138, 95, 74),
    "corpus callosum": (97, 113, 158),
    "posterior commissure": (126, 161, 197),
    "cerebellar white matter": (194, 195, 164),
    "CSF space": (85, 188, 255),
    "ventricles of brain": (88, 106, 215),
    "right lateral ventricle": (88, 106, 215),
    "left lateral ventricle": (88, 106, 215),
    "right third ventricle": (88, 106, 215),
    "left third ventricle": (88, 106, 215),
    "cerebral aqueduct": (88, 106, 215),
    "fourth ventricle": (88, 106, 215),
    "subarachnoid space": (88, 106, 215),
    "spinal cord": (244, 214, 49),
    "gray matter of spinal cord": (200, 200, 215),
    "white matter of spinal cord": (250, 250, 225),
    "endocrine system of brain": (82, 174, 128),
    "pituitary gland": (57, 157, 110),
    "adenohypophysis": (60, 143, 83),
    "neurohypophysis": (92, 162, 109),
    "meninges": (255, 244, 209),
    "dura mater": (255, 244, 209),
    "arachnoid": (255, 244, 209),
    "pia mater": (255, 244, 209),
    "muscles of head": (201, 121, 77),
    "salivary glands": (70, 163, 117),
    "lips": (188, 91, 95),
    "nose": (177, 122, 101),
    "tongue": (166, 84, 94),
    "soft palate": (182, 105, 107),
    "right inner ear": (229, 147, 118),
    "left inner ear": (229, 147, 118),
    "right external ear": (174, 122, 90),
    "left external ear": (174, 122, 90),
    "right middle ear": (201, 112, 73),
    "left middle ear": (201, 112, 73),
    "right eyeball": (194, 142, 0),
    "left eyeball": (194, 142, 0),
    "skull": (241, 213, 144),
    "right frontal bone": (203, 179, 77),
    "left frontal bone": (203, 179, 77),
    "right parietal bone": (229, 204, 109),
    "left parietal bone": (229, 204, 109),
    "right temporal bone": (255, 243, 152),
    "left temporal bone": (255, 243, 152),
    "right sphenoid bone": (209, 185, 85),
    "left sphenoid bone": (209, 185, 85),
    "right ethmoid bone": (248, 223, 131),
    "left ethmoid bone": (248, 223, 131),
    "occipital bone": (255, 230, 138),
    "maxilla": (196, 172, 68),
    "right zygomatic bone": (255, 255, 167),
    "right lacrimal bone": (255, 250, 160),
    "vomer bone": (255, 237, 145),
    "right palatine bone": (242, 217, 123),
    "left palatine bone": (242, 217, 123),
    "mandible": (222, 198, 101),
    "neck": (177, 122, 101),
    "muscles of neck": (213, 124, 109),
    "pharynx": (184, 105, 108),
    "larynx": (150, 208, 243),
    "thyroid gland": (62, 162, 114),
    "right parathyroid glands": (62, 162, 114),
    "left parathyroid glands": (62, 162, 114),
    "skeleton of neck": (242, 206, 142),
    "hyoid bone": (250, 210, 139),
    "cervical vertebral column": (255, 255, 207),
    "thorax": (177, 122, 101),
    "trachea": (182, 228, 255),
    "bronchi": (175, 216, 244),
    "right lung": (197, 165, 145),
    "left lung": (197, 165, 145),
    "superior lobe of right lung": (172, 138, 115),
    "superior lobe of left lung": (172, 138, 115),
    "middle lobe of right lung": (202, 164, 140),
    "inferior lobe of right lung": (224, 186, 162),
    "inferior lobe of left lung": (224, 186, 162),
    "pleura": (255, 245, 217),
    "heart": (206, 110, 84),
    "right atrium": (210, 115, 89),
    "left atrium": (203, 108, 81),
    "atrial septum": (233, 138, 112),
    "ventricular septum": (195, 100, 73),
    "right ventricle of heart": (181, 85, 57),
    "left ventricle of heart": (152, 55, 13),
    "mitral valve": (159, 63, 27),
    "tricuspid valve": (166, 70, 38),
    "aortic valve": (218, 123, 97),
    "pulmonary valve": (225, 130, 104),
    "aorta": (224, 97, 76),
    "pericardium": (255, 244, 209),
    "pericardial cavity": (184, 122, 154),
    "esophagus": (211, 171, 143),
    "thymus": (47, 150, 103),
    "mediastinum": (255, 244, 209),
    "skin of thoracic wall": (173, 121, 88),
    "muscles of thoracic wall": (188, 95, 76),
    "skeleton of thorax": (255, 239, 172),
    "thoracic vertebral column": (226, 202, 134),
    "ribs": (253, 232, 158),
    "sternum": (244, 217, 154),
    "right clavicle": (205, 179, 108),
    "left clavicle": (205, 179, 108),
    "abdominal cavity": (186, 124, 161),
    "abdomen": (177, 122, 101),
    "peritoneum": (255, 255, 220),
    "omentum": (234, 234, 194),
    "peritoneal cavity": (204, 142, 178),
    "retroperitoneal space": (180, 119, 153),
    "stomach": (216, 132, 105),
    "duodenum": (255, 253, 229),
    "small bowel": (205, 167, 142),
    "colon": (204, 168, 143),
    "anus": (255, 224, 199),
    "liver": (221, 130, 101),
    "biliary tree": (0, 145, 30),
    "gallbladder": (139, 150, 98),
    "pancreas": (249, 180, 111),
    "spleen": (157, 108, 162),
    "urinary system": (203, 136, 116),
    "right kidney": (185, 102, 83),
    "left kidney": (185, 102, 83),
    "right ureter": (247, 182, 164),
    "left ureter": (247, 182, 164),
    "urinary bladder": (222, 154, 132),
    "urethra": (124, 186, 223),
    "right adrenal gland": (249, 186, 150),
    "left adrenal gland": (249, 186, 150),
    "female internal genitalia": (244, 170, 147),
    "uterus": (255, 181, 158),
    "right fallopian tube": (255, 190, 165),
    "left fallopian tube": (227, 153, 130),
    "right ovary": (213, 141, 113),
    "left ovary": (213, 141, 113),
    "vagina": (193, 123, 103),
    "male internal genitalia": (216, 146, 127),
    "prostate": (230, 158, 140),
    "right seminal vesicle": (245, 172, 147),
    "left seminal vesicle": (245, 172, 147),
    "right deferent duct": (241, 172, 151),
    "left deferent duct": (241, 172, 151),
    "skin of abdominal wall": (177, 124, 92),
    "muscles of abdominal wall": (171, 85, 68),
    "skeleton of abdomen": (217, 198, 131),
    "lumbar vertebral column": (212, 188, 102),
    "female external genitalia": (185, 135, 134),
    "male external genitalia": (185, 135, 134),
    "skeleton of upper limb": (198, 175, 125),
    "muscles of upper limb": (194, 98, 79),
    "right upper limb": (177, 122, 101),
    "left upper limb": (177, 122, 101),
    "right shoulder": (177, 122, 101),
    "left shoulder": (177, 122, 101),
    "right arm": (177, 122, 101),
    "left arm": (177, 122, 101),
    "right elbow": (177, 122, 101),
    "left elbow": (177, 122, 101),
    "right forearm": (177, 122, 101),
    "left forearm": (177, 122, 101),
    "right wrist": (177, 122, 101),
    "left wrist": (177, 122, 101),
    "right hand": (177, 122, 101),
    "left hand": (177, 122, 101),
    "skeleton of lower limb": (255, 238, 170),
    "muscles of lower limb": (206, 111, 93),
    "right lower limb": (177, 122, 101),
    "left lower limb": (177, 122, 101),
    "right hip": (177, 122, 101),
    "left hip": (177, 122, 101),
    "right thigh": (177, 122, 101),
    "left thigh": (177, 122, 101),
    "right knee": (177, 122, 101),
    "left knee": (177, 122, 101),
    "right leg": (177, 122, 101),
    "left leg": (177, 122, 101),
    "right foot": (177, 122, 101),
    "left foot": (177, 122, 101),
    "peripheral nervous system": (216, 186, 0),
    "autonomic nerve": (255, 226, 77),
    "sympathetic trunk": (255, 243, 106),
    "cranial nerves": (255, 234, 92),
    "vagus nerve": (240, 210, 35),
    "peripheral nerve": (224, 194, 0),
    "circulatory system": (213, 99, 79),
    "systemic arterial system": (217, 102, 81),
    "systemic venous system": (0, 147, 202),
    "pulmonary arterial system": (0, 122, 171),
    "pulmonary venous system": (186, 77, 64),
    "lymphatic system": (111, 197, 131),
    "needle": (240, 255, 30),
    "region 0": (185, 232, 61),
    "region 1": (0, 226, 255),
    "region 2": (251, 159, 255),
    "region 3": (230, 169, 29),
    "region 4": (0, 194, 113),
    "region 5": (104, 160, 249),
    "region 6": (221, 108, 158),
    "region 7": (137, 142, 0),
    "region 8": (230, 70, 0),
    "region 9": (0, 147, 0),
    "region 10": (0, 147, 248),
    "region 11": (231, 0, 206),
    "region 12": (129, 78, 0),
    "region 13": (0, 116, 0),
    "region 14": (0, 0, 255),
    "region 15": (157, 0, 0),
    "unknown": (100, 100, 130),
    "cyst": (205, 205, 100),
}
