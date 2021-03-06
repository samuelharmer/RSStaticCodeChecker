import lib.lib as lib
import json
def easyCheck(s):
    return "CreateBiomechanicalDeformableRegistrationGroup" in s
def scoreForDict(d):
    import sys
    if not isinstance(d, dict):
        return sys.maxint
    arguments_right_result = argumentsRight(d)
    if arguments_right_result != True:
        return (float(arguments_right_result) + float(prefixScore(d)))/2.0
    return sys.maxint
def argumentsRight(d):
    args = ["RegistrationGroupName","ReferenceExaminationName","TargetExaminationNames","ControllingRois","DeformationGridVoxelSize"]
    too_many = []
    for keyword in d.get("keywords", []):
        if keyword.get("arg") in args:
            args.remove(keyword.get("arg"))
        else:
            too_many.append(keyword.get("arg"))
    if not too_many and not args:
        return True
    return (0 if too_many else 3)
def prefixScore(d):
    import sys
    score = sys.maxint
    steps = 0
    if not d.get("_PyType") == "Call":
        return sys.maxint
    _d = d.get("func")
    score = dictMatchScore_0(_d)
    if score != sys.maxint:
        return score
    return sys.maxint
def dictMatchScore_0(d):
    import sys
    score = 0
    steps = 0
    from bases import score_PatientDB
    steps += 1
    score_temp = lib.score_generic(d, "CreateBiomechanicalDeformableRegistrationGroup")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value"), "PatientModel")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value"), "[]")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = lib.score_generic(d.get("value").get("value").get("value"), "TemplatePatientModels")
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    steps += 1
    score_temp = score_PatientDB.get_score(d.get("value").get("value").get("value").get("value"))
    if score_temp == sys.maxint:
        return sys.maxint
    else:
        score += score_temp
    return float(score) / float(steps)
def get_info():
    return json.loads("{\"base\": \"PatientDB.TemplatePatientModels.[].PatientModel\", \"params\": [\"RegistrationGroupName\", \"ReferenceExaminationName\", \"TargetExaminationNames\", \"ControllingRois\", \"DeformationGridVoxelSize\"], \"method\": \"CreateBiomechanicalDeformableRegistrationGroup\", \"description\": \"CreateBiomechanicalDeformableRegistrationGroup(..)\\r\\n  Creates a deformable registration group with biomechanical \\r\\n  deformable registrations for the selected reference examination \\r\\n  and target examinations.\\r\\n  Parameters:\\r\\n    RegistrationGroupName - A registration group with this \\r\\n      name is created.\\r\\n    ReferenceExaminationName - The examination where the \\r\\n      deformation field is defined.\\r\\n    TargetExaminationNames - The examinations the deformation \\r\\n      fields will point to.\\r\\n    ControllingRois - The list with controlling ROIs.\\r\\n    DeformationGridVoxelSize - The deformation grid voxel size \\r\\n      in the DICOM patient-based coordinate system.\\r\\n\"}")
