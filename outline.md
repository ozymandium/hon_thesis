<!-- Honors Thesis Outline
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

## Chap 1: Introduction/Background/DRTK  ##
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
    - velocities   -->

Honors Thesis: Important Updates
================================

## Chap 2: Graphical User Interface ##
    
- __Introductory remarks__
    - What is the role of the gui?
        - [figure] Depict GUI as a block with defined inputs & outputs
        - convey distance and deviation info
            - colors: reference Color state calc section below
    -  2 GUIS were made
        -  monolith
            -  follower-centric
            -  minimalist design geared for quick glance by a busy driver...
        -  Earth
            -  transition via: reason - Mike's comments
            -  mention reason for discarding QGIS as possibility
            -  reference interpolator section, was needed as a result
    - briefly discuss development process
        - using playback of raw data:
            - refine DRTK/TDCP at the same time as the GUI
        - live testing used mostly to ensure proper memory usage and peripheral software/hardware setup correctly
- __Interpolator__
    - introductory paragraph
        - needed when using Earth, b/c choppiness @ 1 Hz limits readability of the screen
        - first tried simple synchronization to slowest data stream, magnitude of jumps still a problem
        - drawback: must induce a 1 timestep lag
    - general algorithm
        - time update
        - linear interp formula
    - path:
        - algorithm for resolving unequal vector lengths
        - interp for each coordinate of each point
    - transition to data dissemanation:
        - did interpolation between middleware and GUI-specific objects
        - designed and tested on Earth GUI, and wanted way to hook up to monolithic GUI
- __Data dissemenation__
    - intro:
        - multiple pieces with each, especially Earth GUI
        - didn't use another database to avoid overhead
    - Qt Signal/Slot
        - how messages arrive from receiver/algos
        - can connect any middleware by providing updates of key info
        - primary means of communication in monolithic GUI
    - Specific to Earth GUI
        - Instance reference passing
        - KML server
- __color state Calculations__
    - Pseudo-code for state determination?
    - use of UTM makes calculations easier, but must be translated to LatLon for GUI
        - reference for coordinate conversion
    - path deviation: user inputs threshold values (simple)
    - distance
        - summation formula
        - projection of deviation point onto path for distance calc
        - what the threshold represents
            - initially wanted input spec to be g's required for stopping
                - required knowing a mu value also, so decided to determine
            - minimum stopping distance (given tire/ground interaction) to the leader's current pos
                - user inputs mu values between tire and pavement - need reference for default values
- __Final Design__
    - qualitative feedback from users which influenced design
    - [figure] arrows pointing to key parts
    - paragraph on each tab of the CMDI
    - how the alerts are raised in each GUI for dst, dev


## Chap 3: Experimental Validation

- __Introductory remarks__

- __Hardware Setup__
    - emphasize portability
    - [photo] Leader hardware
    - [photo] follower hardware

- __Description of Tests for the GUI__
    - Lane change replication
        - leader goes around curve then changes lanes between any of serveral cones
        - follower cannot see the lane change when it occurs
        - must change lanes between the correct pair of cones
        - provides definitive yes/no results: binary scoring scheme
        - *what specifically does this test?*
    - Skid Pad
        - no visual cues
        - *hard to replicate path between drivers for consistency...*
        - scoring scheme will need an integral
    - circuit around NCAT track, parkinglot
        - driver tries to stay as close as possible without getting too close
        - change speeds
        - 2 scenarios with same circuit and same drivers
            - Nighttime : "Impaired visibility"
            - Daytime
        - compare day to night
        - scoring scheme will be piecewise with integrals
    - Track Loop Twice
        - lane change locations known to leader
        - follower try to maintain constant distance
        - Scoring scheme penalizes being too close much more than being too far
        - examine "steady state" path deviation
- __Results post-processing explanation__
- __Results__: tables, figures ...
- __Results discussion__
    - Examine data if/when GUI went offline then came back and draw conclusions




<!-- ## Chap 4: Extension to Longer Chains ##
- Daisy chain with a set configuration
- Simulate with 3 Vehicles, test?


## Chap 5: Conclusions ##
- Evaluation of DRTK in convoys
    - accuracy behavior
    -limitations
-  Future Work 
    - Very Long chains (~10 vehicles) -->