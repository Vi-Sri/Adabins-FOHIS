import const

# atmosphere model TODO : fog model automation
const.VISIBILITY_RANGE_MOLECULE = 0.5 # m    12
const.VISIBILITY_RANGE_AEROSOL = 100  # m     450
const.ECM = 1 / const.VISIBILITY_RANGE_MOLECULE  # EXTINCTION_COEFFICIENT_MOLECULE /m
const.ECA = 1 / const.VISIBILITY_RANGE_AEROSOL  # EXTINCTION_COEFFICIENT_AEROSOL /m

const.FT = 100  # FOG_TOP m  31  70
const.HT = 80  # HAZE_TOP m  300    34

# camera
const.CAMERA_ALTITUDE = 1  #  m fog 50   1.8
const.HORIZONTAL_ANGLE = 0  #  °
const.CAMERA_VERTICAL_FOV = 64  #  °


