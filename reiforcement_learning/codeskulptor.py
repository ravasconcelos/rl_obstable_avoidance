
import simpleguitk as simplegui
import math
import random
import term_project_monte_carlo_dynamic as montecarlo

#define constants

#master_policy={0: {0: {(0, 0): 'R', (0, 1): 'R', (0, 2): 'R', (0, 3): 'D', (1, 0): 'D', (1, 1): 'L', (1, 2): 'U', (1, 3): 'D', (2, 0): 'R', (2, 1): 'D', (2, 2): 'D', (2, 3): 'D', (3, 0): 'R', (3, 1): 'R', (3, 2): 'R', (3, 3): 'U'}, 1: {(0, 0): 'R', (0, 1): 'R', (0, 2): 'R', (0, 3): 'D', (1, 0): 'D', (1, 1): 'R', (1, 2): 'R', (1, 3): 'D', (2, 0): 'D', (2, 1): 'L', (2, 2): 'R', (2, 3): 'D', (3, 0): 'R', (3, 1): 'R', (3, 2): 'R', (3, 3): 'U'}, 2: {(0, 0): 'R', (0, 1): 'R', (0, 2): 'D', (0, 3): 'D', (1, 0): 'U', (1, 1): 'R', (1, 2): 'R', (1, 3): 'D', (2, 0): 'R', (2, 1): 'D', (2, 2): 'R', (2, 3): 'D', (3, 0): 'U', (3, 1): 'R', (3, 2): 'R', (3, 3): 'U'}, 3: {(0, 0): 'R', (0, 1): 'R', (0, 2): 'R', (0, 3): 'D', (1, 0): 'U', (1, 1): 'R', (1, 2): 'R', (1, 3): 'D', (2, 0): 'U', (2, 1): 'D', (2, 2): 'R', (2, 3): 'D', (3, 0): 'R', (3, 1): 'R', (3, 2): 'R', (3, 3): 'U'}}, 1: {0: {(0, 0): 'R', (0, 1): 'R', (0, 2): 'R', (0, 3): 'D', (1, 0): 'R', (1, 1): 'D', (1, 2): 'R', (1, 3): 'D', (2, 0): 'D', (2, 1): 'D', (2, 2): 'D', (2, 3): 'D', (3, 0): 'R', (3, 1): 'R', (3, 2): 'R', (3, 3): 'U'}, 1: {(0, 0): 'D', (0, 1): 'L', (0, 2): 'R', (0, 3): 'D', (1, 0): 'D', (1, 1): 'D', (1, 2): 'D', (1, 3): 'D', (2, 0): 'D', (2, 1): 'D', (2, 2): 'D', (2, 3): 'D', (3, 0): 'R', (3, 1): 'R', (3, 2): 'R', (3, 3): 'U'}, 2: {(0, 0): 'D', (0, 1): 'L', (0, 2): 'L', (0, 3): 'D', (1, 0): 'D', (1, 1): 'D', (1, 2): 'R', (1, 3): 'D', (2, 0): 'R', (2, 1): 'D', (2, 2): 'L', (2, 3): 'D', (3, 0): 'R', (3, 1): 'R', (3, 2): 'R', (3, 3): 'U'}, 3: {(0, 0): 'R', (0, 1): 'D', (0, 2): 'D', (0, 3): 'L', (1, 0): 'D', (1, 1): 'D', (1, 2): 'D', (1, 3): 'L', (2, 0): 'D', (2, 1): 'R', (2, 2): 'R', (2, 3): 'D', (3, 0): 'R', (3, 1): 'R', (3, 2): 'R', (3, 3): 'U'}}, 2: {0: {(0, 0): 'R', (0, 1): 'R', (0, 2): 'D', (0, 3): 'D', (1, 0): 'R', (1, 1): 'R', (1, 2): 'D', (1, 3): 'D', (2, 0): 'D', (2, 1): 'R', (2, 2): 'R', (2, 3): 'D', (3, 0): 'R', (3, 1): 'R', (3, 2): 'R', (3, 3): 'U'}, 1: {(0, 0): 'R', (0, 1): 'R', (0, 2): 'R', (0, 3): 'D', (1, 0): 'U', (1, 1): 'R', (1, 2): 'D', (1, 3): 'D', (2, 0): 'D', (2, 1): 'L', (2, 2): 'R', (2, 3): 'D', (3, 0): 'R', (3, 1): 'R', (3, 2): 'R', (3, 3): 'U'}, 2: {(0, 0): 'R', (0, 1): 'R', (0, 2): 'R', (0, 3): 'D', (1, 0): 'D', (1, 1): 'U', (1, 2): 'R', (1, 3): 'D', (2, 0): 'D', (2, 1): 'D', (2, 2): 'R', (2, 3): 'D', (3, 0): 'R', (3, 1): 'R', (3, 2): 'R', (3, 3): 'U'}, 3: {(0, 0): 'R', (0, 1): 'D', (0, 2): 'D', (0, 3): 'L', (1, 0): 'U', (1, 1): 'D', (1, 2): 'D', (1, 3): 'L', (2, 0): 'U', (2, 1): 'R', (2, 2): 'D', (2, 3): 'D', (3, 0): 'R', (3, 1): 'R', (3, 2): 'R', (3, 3): 'U'}}, 3: {0: {(0, 0): 'R', (0, 1): 'R', (0, 2): 'D', (0, 3): 'D', (1, 0): 'U', (1, 1): 'U', (1, 2): 'D', (1, 3): 'D', (2, 0): 'U', (2, 1): 'D', (2, 2): 'R', (2, 3): 'D', (3, 0): 'R', (3, 1): 'R', (3, 2): 'R', (3, 3): 'U'}, 1: {(0, 0): 'R', (0, 1): 'R', (0, 2): 'R', (0, 3): 'D', (1, 0): 'U', (1, 1): 'D', (1, 2): 'R', (1, 3): 'D', (2, 0): 'R', (2, 1): 'R', (2, 2): 'D', (2, 3): 'D', (3, 0): 'U', (3, 1): 'R', (3, 2): 'R', (3, 3): 'U'}, 2: {(0, 0): 'R', (0, 1): 'R', (0, 2): 'D', (0, 3): 'D', (1, 0): 'R', (1, 1): 'R', (1, 2): 'R', (1, 3): 'D', (2, 0): 'U', (2, 1): 'U', (2, 2): 'R', (2, 3): 'D', (3, 0): 'R', (3, 1): 'U', (3, 2): 'R', (3, 3): 'U'}, 3: {(0, 0): 'D', (0, 1): 'D', (0, 2): 'R', (0, 3): 'D', (1, 0): 'R', (1, 1): 'R', (1, 2): 'R', (1, 3): 'D', (2, 0): 'U', (2, 1): 'D', (2, 2): 'D', (2, 3): 'D', (3, 0): 'U', (3, 1): 'R', (3, 2): 'R', (3, 3): 'U'}}}
master_policy={}

OBSTACLE_RAD = 20 # how big (radius) are the obstacles
ROBOT_RAD = 30 # how big (radius) is the robot?
SENSOR_FOV = 10.0 # FOV of each sensor THIS MUST BE A FLOAT!!!!!! 
SENSOR_MAX_R = 100 # max range that each sensor can report
SENSOR_ALERT_R = 50 #range within which sensor reports are acted upon
TURN_SCALE_FACTOR = 2 # how drastic do we want the turns to be
SAFETY_DISTANCE = 50
#helper functions

#print (f"returned policy={montecarlo.calculate_gridworld_policy([(2,1)])}")

def find_location_onMap(pos):
  location_in_the_grid=[]
  location_in_the_map=[]
  i=0
  i1=0
  loc=0
  loc1=0
  for squares in range(0,10):
    i1=0
    for quare in range(0,10):
      loc=0
      #square.append((i,i1))
      if ((pos[0]>i and pos[0]<=i+50) and (pos[1]>i1 and pos[1]<=i1+50)):
        for rows in range(0,4):
          loc1=0
          for col in range(0,4):
            if ((pos[0]>loc+i and pos[0]<=loc+i+12.5) and (pos[1]>loc1+i1 and pos[1]<=loc1+12.5+i1)):           
              location_in_the_grid.append(loc)
              location_in_the_grid.append(loc1)
              location_in_the_map.append(i)
              location_in_the_map.append(i1)
            
            loc1+=12.5
          loc+=12.5
      i1+=50
    i+=50

#To to convert to 3x3 grid
  location_in_the_grid[0]=int(location_in_the_grid[0]/12.5)
  location_in_the_grid[1]=int(location_in_the_grid[1]/12.5)
#To to convert to 5x5 map each sqaure is 100X100 pixel
  location_in_the_map[0]=int(location_in_the_map[0]/50)
  location_in_the_map[1]=int(location_in_the_map[1]/50)
  return location_in_the_map, location_in_the_grid


def dynamic_policy_finder (mylocation,obs):
  print(f"mylocation={mylocation}, obs={obs}")
  mylocation_onMap, my_location_onGrid = find_location_onMap(mylocation)
  print(f"mylocation_onMap={mylocation_onMap}, my_location_onGrid={my_location_onGrid}")
  obs_location_onMap, obs_location_onGrid = find_location_onMap(obs)
  print(f"obs_location_onMap={obs_location_onMap}, obs_location_onGrid={obs_location_onGrid}")
  if (mylocation_onMap == obs_location_onMap):
    print("mylocation_onMap == obs_location_onMap")

    end_state = (3,3)
    if (obs_location_onGrid[0],obs_location_onGrid[1]) == end_state:
      end_state = (3,2)

    policy_key = f"{end_state}|({obs_location_onGrid[0]},{obs_location_onGrid[1]})"
    print(f"policy_key={policy_key}")

    if policy_key in master_policy:
        policy = master_policy[policy_key]
    else:
        policy = montecarlo.calculate_gridworld_policy(end_state,[(obs_location_onGrid[0],obs_location_onGrid[1])])
        master_policy[policy_key] = policy

    #policy= master_policy[obs_location_onGrid[0]][obs_location_onGrid[1]]
    direction = policy.get((my_location_onGrid[0],my_location_onGrid[1]), ' ')
    print(f"direction={direction}")
    return direction
  else:
    return None


def policy_finder (mylocation,obs):
  mylocation_onMap, my_location_onGrid = find_location_onMap(mylocation)
  obs_location_onMap, obs_location_onGrid = find_location_onMap(obs)
  if (mylocation_onMap == obs_location_onMap):
    print("Match found")
    policy= master_policy[obs_location_onGrid[0]][obs_location_onGrid[1]]
    direction = policy.get((my_location_onGrid[0],my_location_onGrid[1]), ' ')
    print(direction)
    return direction
  else:
    return None

def rel_brg_fm_offset_sensor(true_hdg, sensor_offset, tgt_brg):
    #given robot's true heading, the sensor offset angle and the
    #true brg of the target, this fn will return the relative brg
    #of the target from the sensor's line of sight
    
    sensor_look_brg = (true_hdg + sensor_offset)%360
    tgt_rel_fm_sensor = tgt_brg - sensor_look_brg

    if tgt_rel_fm_sensor < -180:
        tgt_rel_fm_sensor += 360
    
    return tgt_rel_fm_sensor

def brg_in_deg(p0, p1):#bearing only in degrees
    [x1, y1] = p0
    [x2, y2] = p1
    a = math.degrees(math.atan((y1 - y2)/(x1 - x2 + 0.000000001)))
    #find and correct the quadrant...
    if  x2 >= x1:
        b = 90 + a
    else:
        b = 270 + a
    return b

def dist(p1, p0):#distance only
    return math.sqrt((p1[0] - p0[0])**2+(p1[1]-p0[1])**2)

def dist_and_brg_in_deg(p0, p1):#bearing and distance in degrees between two points
    [x1, y1] = p0
    [x2, y2] = p1
    r = math.sqrt((x1 - x2)**2 + (y1 - y2)**2) # distance
    a = math.degrees(math.atan((y1 - y2)/(x1 - x2 + 0.000000001)))
    #find and correct the quadrant...
    if  x2 >= x1:
        b = 90 + a
    else:
        b = 270 + a
    return r, b

def angle_to_vector(ang):#resolve angles into vectors
    ang = math.radians(ang)
    return [math.cos(ang), math.sin(ang)]

def relative_brg(b1, b2):
    rb = b2 - b1
    if rb > 180:
        rb = 360 - rb
    if rb < -180:
        rb += 360
        rb *= -1
    return rb

def create_vector(from_pos, length, brg):       
        u_vec = angle_to_vector(brg)
        #print "generating target line..."
        vec0 = from_pos[0] + length * u_vec[1] 
        vec1 = from_pos[1] - length * u_vec[0]
        
        return [vec0, vec1]

    
#define classes

class Sonar:
    def __init__(self, index, FOV, max_r, robot_co):
        #create a instance of this class
        self.pos = [0,0]
        self.index = index
        self.max_r = max_r
        self.offset =  index * FOV #+ FOV/2 # on what relative bearing is this sensor looking?
        self.look_brg = (robot_co + self.offset)%360
        self.vec = [0,0] # just a vector for grpahical ouptut of pings
        self.has_valid_echo = False #indicates if this sonar has a "valid" obstacle in sight
        #print "Creating Sonar:" , index, " offset ", self.offset, "true LOS:", self.look_brg
            
    def ping_actual():#ping for real in a robot and return range observed
        pass
    
    def ping_simulated(self, obstacle_list, robot_co):
        #from robot position and robot_co, run through obs_list
        #return the distance to closest object within 
        #FOV and within self.max_r of THIS SENSOR
        # range all the obstacles in view, find the nearest
        
        range_list = []
        
        for obs in obstacle_list:# find objects within max_r and inside FOV
            #print "pinging for robot_co:", robot_co
            can_observe, d = self.can_observe(robot_co, obs, OBSTACLE_RAD)
            #print can_observe, d
            if can_observe:
                range_list.append(d) 
        if len(range_list) > 0:
            self.output = min(range_list)- SAFETY_DISTANCE
        else:
            self.output = SENSOR_MAX_R
        #print "closest point: " , obs , " distance:", self.output
    
    def get_output(self):
        return self.output
    
    def can_observe(self, robot_co, obstacle_pos, obstacle_rad):
        #if obstacle is within within the max_r of the sensor
        #and within FOV, return True and the distance observed
        #else return False, 0
        
        dist, brg = dist_and_brg_in_deg(self.pos, obstacle_pos)
        
        if dist < self.max_r: #if the object is within max_r....
            rel_brg = rel_brg_fm_offset_sensor(robot_co, self.offset, brg)#rel brg of tgt from sensor LOS
            print(f"dist={dist}, rel_brg={rel_brg}")
            rel_brg_radians = math.radians(rel_brg)
            print(f"rel_brg_radians={rel_brg_radians}")
            if rel_brg_radians < -1 or rel_brg_radians > 1:
                return False, 0
            print(f"math.asin(math.radians(rel_brg))={math.asin(math.radians(rel_brg))}")
            print(f"abs(dist * math.asin(math.radians(rel_brg)))={abs(dist * math.asin(math.radians(rel_brg)))}")
            d_test = abs(dist * math.asin(math.radians(rel_brg)))
            if d_test < OBSTACLE_RAD + ROBOT_RAD: 
                self.has_valid_echo = True
                return True, dist # if the object is within min allowed lateral separation
            else:
                self.has_valid_echo = False
                return False, 0 # ignore it
        else:#if the object is outside max_r of this sonar...ignore it
            self.has_valid_echo = False
            return False, 0
      
    def update(self, platform_pos, platform_co, obstacle_list):
              
        #update own parameters
        self.pos = platform_pos
        
        self.look_brg = (platform_co + self.offset)%360
        
        #calculate output of this sensor
        
        self.ping_simulated(obstacle_list, platform_co)
        
        self.vec = create_vector(self.pos, self.output + ROBOT_RAD, self.look_brg)#calculate distance vector for drawing on canvas
        
        #print "sensor index:", self.index, " look brg:", self.look_brg
    def draw(self, canvas): # draw the sensor's output
        #if self.has_valid_echo:
        canvas.draw_line(self.pos,self.vec, 1, 'lime')
        canvas.draw_text(str(self.index),(self.vec[0]+4, self.vec[1]+4), 10, "lime"),
        #print self.index, " VE:" , self.has_valid_echo
        
class Sonar_Array:
    def __init__(self, n_sensors, SENSOR_FOV, SENSOR_MAX_R, robot_co):
        self.sonar_list = []
        self.need_diversion_flag = False
        
        i_pos = list(range(1, int(n_sensor/2) + 1))
        i_neg = list(range(int(-n_sensor/2) , 0))
        i_pos.reverse()
        i_neg.reverse()
        i_pos.extend(i_neg)
        
        for i in i_pos:#create a list of individual sonars...
            self.sonar_list.append(Sonar(i, SENSOR_FOV, SENSOR_MAX_R, robot_co))
   
    def update(self, robot_pos, robot_co, obstacle_list, method):
        #update sonar array
        for sonar in self.sonar_list:#update output of each sensor
            sonar.update(robot_pos, robot_co, obstacle_list)
            
        if method == "w_sum":#process data by method of weighted sums
            return self.weighted_sum_method(robot_pos, robot_co)
    
    def weighted_sum_method(self, robot_pos, robot_co):
        #process data by the weighted sum method and 
        #return (1) whether turn is required or not (2) index of recommended sonar LOS to turn to
        sum_d = 0
        sum_wt = 0
        alert = False
        #print "checking all sonars:"      
        for sonar in self.sonar_list:
            #print "sonar:", sonar.index, " range:", sonar.output
            if sonar.output < SENSOR_ALERT_R:#has this sonar found anything in danger zone?
                alert = True
                #print "obstacle found by index ", sonar.index
                for s1 in self.sonar_list: #process the whole array
                    d = int(s1.output)
                    gain = 1#SENSOR_MAX_R/(SENSOR_MAX_R - d)
                    sum_d +=  d
                    sum_wt += s1.index * d * gain
                    #print "I:", s1.index,",D:",int(s1.output), ",sum_D:", sum_d, "sum_wt:",sum_wt
                rec_index = math.ceil(TURN_SCALE_FACTOR * float(sum_wt)/sum_d) #index of sonar with best LOS
                #rec_index = int(TURN_SCALE_FACTOR * float(sum_d)/sum_wt)
                print("Rec index:", rec_index)
                if abs(rec_index) > n_sensor/2:
                    print("rec index too large")
                    rec_index = n_sensor/2
#                    if rec_index < 0:
#                        rec_index = -n_sensor/2
#                    else:
#                        rec_index = n_sensor/2
                print("Rec index:", rec_index) 
                break # processing completed
            else: #no obstacle in danger zone
                rec_index = 0
                #return robot_co, False
                #print : index = ", sonar.index
        #print "break from loop."
        if rec_index == 0 and alert == True:
            print("alert with no alteration")
            for obs in full_obstacle_list:
                    mylocation=robot_pos
                    mylocation_onMap, my_location_onGrid = find_location_onMap(mylocation)
                    obs_location_onMap, obs_location_onGrid = find_location_onMap(obs)
                    action=None
                    if (mylocation_onMap == obs_location_onMap):
                        #action = policy_finder(mylocation,obs)
                        action = dynamic_policy_finder(mylocation,obs)
                        if action != None:
                            if action == 'R':
                                offset=90
                            elif action == 'D':
                                offset=180
                            elif action == 'L':
                                offset=270
                            elif action == 'U':
                                offset = 359
                        break
            if (action !=None):
                print(robot_pos)
                print("*********")
                print(((offset%robot_co)+robot_co))
                print("******")
                return (offset%robot_co)+robot_co, True 
            else:
               return robot_co, True    
                
        elif abs(rec_index) > 0: # some alteration recommended
            print("turn recommended")
            offset =  rec_index * SENSOR_FOV #how much is the angular offset  
            for obs in full_obstacle_list:
                mylocation=robot_pos
                mylocation_onMap, my_location_onGrid = find_location_onMap(mylocation)
                obs_location_onMap, obs_location_onGrid = find_location_onMap(obs)
                action=None
                if (mylocation_onMap == obs_location_onMap):
                    #action = policy_finder(mylocation,obs)
                    action = dynamic_policy_finder(mylocation,obs)
                    if action != None:
                        if action == 'R':
                            offset=90
                        elif action == 'D':
                            offset=180
                        elif action == 'L':
                            offset=270
                        elif action == 'U':
                            offset = 359
                    break
            print(robot_pos)
            print("*********")
            print(action)
            print(((offset%robot_co)+robot_co))
            print("******")
            if (action==None):
               return robot_co, False 
            return (offset%robot_co), True
        else:# no diversion needed
            print("no alert no diversion")
            return robot_co, False
    
    def draw(self, canvas):
        for sonar in self.sonar_list:
            sonar.draw(canvas)

class Robot:
    def __init__(self, pos, co, n_sensor):
        self.pos = pos
        self.history = [pos]
        self.co = co
        self.spd = 10 # robot speed in pixels/ step
        self.s_array = Sonar_Array(n_sensor, SENSOR_FOV, SENSOR_MAX_R, self.co)
        self.goal_brg = brg_in_deg(self.pos, goal_pos)
        self.obstacles_in_view = []
    
    def get_obstacles_in_view(self):
        return self.obstacles_in_view
    
    def update(self):
        self.obstacles_in_view = [] #delete all the old obstacles in view
        for obs in full_obstacle_list:
            if dist(self.pos, obs) < SENSOR_MAX_R:
                self.obstacles_in_view.append(obs)
                
        #re-calculate direction to goal
        self.goal_brg = brg_in_deg(self.pos, goal_pos)
        #re-estimate sensor output by weighted sum method
        co1, need_turn = self.s_array.update(self.pos, self.goal_brg, self.obstacles_in_view, "w_sum")
        #print "Path Clear:", self.path_is_clear()
        if self.path_is_clear():#can we reach the goal directly from here?
            self.co = brg_in_deg(self.pos, goal_pos)
            print("path clear. ignoring recommendation")
        elif need_turn: #do we need to turn
            self.co = co1
            print("path not clear. following recommendation")
        else: # path is not fully clear, but there are no immediate obstacles
            pass
            #self.co = brg_in_deg(self.pos, goal_pos)

        #m5e the robot by one step...
        self.move(2)
        print(f"master_policy.keys()={master_policy.keys()}")

    def path_is_clear(self):#return True if there is a clear path to the goal
        goal_brg = brg_in_deg(self.pos, goal_pos)
        for obs in self.obstacles_in_view:
            if dist(self.pos, goal_pos) > dist(self.pos, obs):
                d_obs, obs_brg = dist_and_brg_in_deg(self.pos, obs)
                rel_brg = abs(relative_brg(goal_brg, obs_brg))

                print(f"rel_brg={rel_brg}")
                rel_brg_radians = math.radians(rel_brg)
                print(f"rel_brg_radians={rel_brg_radians}")
                if rel_brg_radians < -1 or rel_brg_radians > 1:
                    return False

                d_lateral = abs(d_obs * math.asin(math.radians(rel_brg)))
                if d_lateral < OBSTACLE_RAD + ROBOT_RAD: 
                    return False
        return True
    
    def move(self, dT):
        print("VVVVVBVV")        
        print((self.co))
        u_vec = angle_to_vector(self.co)
        
        self.pos[0] += self.spd * dT * u_vec[1]
        self.pos[1] -= self.spd * dT * u_vec[0]
        
        self.history.append([self.pos[0], self.pos[1]])
        
    def get_pos(self):
        return self.pos
    
    def set_pos(self, pos):
        self.pos = pos
    
    def set_co(self, co):
        self.co = co
        #print "setting robot co:", self.co
    
    def delete_history(self):
        self.history = []
   
    def draw(self, canvas):
        #Draw the robot
        canvas.draw_circle(self.pos, 4, 3, "yellow")
        canvas.draw_text("R", [self.pos[0] + 10, self.pos[1] +10], 16, "yellow")
        #Draw brg line to goal
        self.goal_vec = create_vector(self.pos, 150, self.goal_brg)
        canvas.draw_line(self.pos, self.goal_vec, 2, "teal")
        #Draw current heading vector
        self.co_vec = create_vector(self.pos, 150, self.co)
        canvas.draw_line(self.pos, self.co_vec, 2, "white")
        #draw the output of the sonar array
        self.s_array.draw(canvas)
        #draw the obstacles in view
        for obs in self.obstacles_in_view:
            canvas.draw_circle(obs,2,1, "red")
            canvas.draw_circle(obs,OBSTACLE_RAD, 1, "green") 
        #draw history
        for point in self.history:
            canvas.draw_circle(point,2,2, "lime")
        
        
#define globals

g_state = "None"

start_pos = [10,10]
robot_pos = [10, 10]
robot_co = 1

goal_pos = [500,500]
#obstacle_list = [(300, 213), (310, 124), (250, 110), (300, 230)]
full_obstacle_list = [(10,200),(250, 110), (200,280),(220,200), (300,300), (200,100), (400,150),(400, 110), 
                 (430, 390), (201, 304), (135, 281), 
                 (286, 373), (175, 280), (250, 375), (139, 327), (369, 278), 
                 (295, 196), (210, 111),(100,100),(110,110),(79,250)]
#create a robot with 6 sensors

n_sensor = 16 

#create a sonar array
#s1 = Sonar_Array(n_sensor, SENSOR_FOV, SENSOR_MAX_R, robot_co)
r1 = Robot(robot_pos, robot_co, n_sensor)

r1.update()
#define event handlers

def click(pos):
    global g_state, start_pos, goal_pos, robot_pos
    if g_state == "Start":
        start_pos = pos
        r1.set_pos(list(pos))
    elif g_state == "Goal":
        goal_pos = pos
        r1.set_co(brg_in_deg(r1.get_pos(), pos))
    elif g_state == "Set Robot":
        r1.set_co(brg_in_deg(r1.get_pos(), pos))
        r1.set_pos(list(pos))
        r1.delete_history()
    elif g_state == "Add Obs":
        full_obstacle_list.append(pos)
        print(full_obstacle_list)
        #update the robot
    r1.update()
    g_state = "None"
        
def set_start():
    global g_state
    g_state = "Start"
    
def set_goal():
    global g_state
    g_state = "Goal"

def set_robot_pos():
    global g_state
    g_state = "Set Robot"

def alter_co(text):
    r1.set_co(float(text))
    r1.update()
            
def draw(canvas):
    #draw start 
    canvas.draw_circle(start_pos, 4, 3, "red")
    canvas.draw_text("S", [start_pos[0] + 10, start_pos[1] +10], 16, "red")
    #draw goal
    canvas.draw_circle(goal_pos, 4, 3, "green")
    canvas.draw_text("G", [goal_pos[0] + 10, goal_pos[1] +10], 16, "green")
    #draw the obstacles
    for obs in full_obstacle_list:
        canvas.draw_circle(obs,2,1, "red")
        canvas.draw_circle(obs,OBSTACLE_RAD, 1, "white") 
    
    #draw sonar lines...
    r1.draw(canvas)

def step():
        r1.update()

def add_obs():
    global g_state
    g_state = "Add Obs"
    
    
#create simplegui controls

f1 = simplegui.create_frame("Obs Avoidance", 500, 500)
#btn_start = f1.add_button("Set Start", set_start, 100)
btn_goal = f1.add_button("Set Goal", set_goal, 100)
btn_robot = f1.add_button("Set Robot", set_robot_pos, 100)
txt_r_co = f1.add_input("Robot Co", alter_co, 100)
btn_step = f1.add_button("Step", step, 100)

btn_add_obs = f1.add_button("Add Obs", add_obs, 100)

f1.set_draw_handler(draw)
f1.set_mouseclick_handler(click)

#start simplegui

f1.start()