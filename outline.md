Honors Thesis Outline
=====================

## Abstract ##
*What was done?*  

- A GUI was developed to aid in driver-assisted automated following  
- Error propagation in convoys was examined  

__*Why this paper is important [one line]*__  
*Why? What questions were answered?*  

- Are DRTK errors in a convoy the same from 1st vehicle to last as that from first vehicle to 2nd?  

*How was it done?*  
*What was learned?* [maybe not applicable except to error propagation]  

## Chap 1: Introduction/Background/DRTK  [Finish by 2/1/2013] ##
- Introductory remarks
    - establish use case
        - convoy
        - where computation is carried out, which vehicles are aware of what
            - each pair's leader computes RPV
            - ideal for gui in all followers, finding the errors
    - mention other nav scenarios
        - swarm mapping
        - mention aerial scenarios
- Motivation - *why driver assistance is necessary*  
    - Convoys 
        - military
            - low visibility conditions
            - narrow path of safe travel (e.g., mines, cliffs, etc.)
        - commercial (tractor trailer)
            - saving money by drafting
            - increase number of vehicles on the road safely -> efficiency
            - driver fatigue, reduce drivers
    - Autonomous scenarios
        - MGV Leader + UGV Follower 
            - don't need driver assistance GUI, but it would help in developing the follower control algorithms
        - DRTK algorithms development
- Other L/F solutions
    - Vision
        - mono camera
            - Principle: size (px) of leader => distance
            - Drawbacks
        - stereo camera
            - Principle: depth from distance between cameras, image differences
            - Drawbacks
    - detection and ranging
        - sonar
            - get no position, only range
            - useless in noisy environments
        - Radar _most popular alternative to DRTK_
            - limited range
            - requires line-of-sight
        - lidar
            - Use of intensity measurement can help with other tasks (lanes)
            -  requires line-of sight
    - advantages of GPS-based
- What comes from DRTK - need to redo
    - TDCP - path accuracy
    - Lateral Dev
    - Distance (direct)
    - velocities  

## Chap 2: Graphical User Interface  [Finish by 2/15/2013] ##
    
- Introductory remarks
    - development using playback
    -  could prove useful in the development of LF control algorithms (out of the scope of this paper)
- Calculations to determine color states
        - use of UTM makes calculations easier, but must be translated to LatLon for GUI
    - path deviation
    - distance
        - projection of deviation point onto path for distance calc
-  Data dissemenation
    - Qt Signal/Slot
    - Instance reference passing
    - didn't use another database to avoid overhead
- Architecture
    - [figure] Depict GUI as a block with defined inputs & outputs
    - global Message passing
        - how messages arrive from receiver - modularity of gui's global messaging interface
        - message structure
        - how messages get from raw data to qt-usable form
    - Threading
- Final Design
    - [figure] arrows pointing to key parts


## Chap 3: Experimental Validation [Finish by 4/1/2013] ##  

- Introductory remarks

- Hardware Setup  
    
- Tests
    - Description of Tests
        - Straight Line
        - Constant Radius, constant velocity
        - Skid Pad?
            - need place with no visual cues
            - hard to replicate path between drivers
    - Processing of Results
        - 


- User Feedback
    - Intro: outline Ft. Benning Demo
    - Test 1: 
    - Test 2: nighttime
        - essentially 
    - Response Session outline

## Chap 4: Extension to Longer Chains [Finish by end of semester]##
- Daisy chain with a set configuration
- Simulate with 3 Vehicles, test?


## Chap 5: Conclusions [Finish by end of semester]##
- Evaluation of DRTK in convoys
    - accuracy behavior
    -limitations
-  Future Work 
    - Very Long chains (~10 vehicles)