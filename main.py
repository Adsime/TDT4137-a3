import funcitons


defArr = range(-10, 11)

# Distance triangle coordinates
smallTri = [1.5, 3.0, 4.5]
perfectTri = [3.5, 5.0, 6.5]

# Delta triangle coordinates
stableTri = [-1.5, 0, 1.5]
growingTri = [0.5, 2, 3.5]

# Action triangle coordinates
slowDownTri = [-7, -4, -1]
noneTri = [-3, 0, 3]
speedUpTri = [1, 4, 7]

# input variables
distance = 3.7
delta = 1.2

# STEP 1: Fuzzification
distanceSmall = funcitons.triangle_val(distance, smallTri, 1)
distancePerfect = funcitons.triangle_val(distance, perfectTri, 1)
deltaStable = funcitons.triangle_val(delta, stableTri, 1)
deltaGrowing = funcitons.triangle_val(delta, growingTri, 1)

# STEP 2: Eval of rules


slowDown = min(distanceSmall, deltaStable)
none = min(distanceSmall, deltaGrowing)
speedUp = min(distancePerfect, deltaGrowing)
floorIt = 0
breakHard = 0

cuts = [slowDown, none, speedUp]

# STEP 3: Aggregation of rules

items = funcitons.aggregate_rules(defArr, [slowDownTri, noneTri, speedUpTri], cuts)



# STEP 4: Defuzzification

position = funcitons.integrate(items)
print(position)
funcitons.plot(defArr, items, position)
