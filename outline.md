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
    - fused and coupled solutions
        - mention FHWA2 work
        - Scott thesis on coupling    
    - advantages of GPS-based
- What comes from DRTK
    - TDCP - path accuracy
    - Lateral Dev
    - Distance (direct)
    - velocities

## Chap 2: Graphical User Interface  [Finish by 2/15/2013] ##
- Introductory remarks
    - development using playback
    -  could prove useful in the development of LF control algorithms (out of the scope of this paper)
- Architecture
    - [figure] Depict GUI as a block with defined inputs & outputs
    - global Message passing
            - how messages arrive from receiver - modularity of gui's global messaging interface
            - message structure
            - how messages get from raw data to qt-usable form
    - Qt message pasing
        - signals/slots
        - connections between renderarea, mainwindow
    - Threading
- Real World
    - method used for validation of screen info
    - usefulness - can a driver use it exclusively?
- Optimization Process
    - Simulation in lab using Logitech controllers
    - Optimize using human subjects
    - Indust. Eng./ Psychology stuff on conveying information
- Final Design
    - [figure] arrows pointing to key parts

## Chap 3: Experimental Validation [Finish by 4/1/2013] ##
*Prowler/Santa Fe?*  
*Record Lateral Errors and Speed consistency*  

- 2 Vehicle - *focus on GUI usefulness*  
- 3 Vehicle - *focus on error propagation*  
    - 

## Chap 4: Extension to Longer Chains [Finish by end of semester]##
- Daisy chain with a set configuration
- Simulate with 3 Vehicles, test?


## Chap 5: Conclusions [Finish by end of semester]##
- Evaluation of DRTK in convoys
    - accuracy behavior
    -limitations
-  Future Work 
    - Very Long chains (~10 vehicles)