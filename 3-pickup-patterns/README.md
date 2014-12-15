NYC Taxi Analysis
========

Scripts to analyze taxi data on Amazon AWS: 3 Pickup patterns

Instruction
-----------

1. Upload taxi trip and fare data to an S3 bucket. For example:
    *  s3://mda2014/taxi/trip

2. Clone this repository and upload the scripts to your bucket on S3. For example:

    * s3://mda2014/3-pickup-patterns

3. To run first mapreduce job, create an Amazon EMR cluster with the following configuration (the bootstrap action is very important -- please pay attention to that):

        * Termination protection: Yes
        * Logging: Enabled
        * Hadoop distribution: Amazon AMI 3.3.1
        * Bootstrap action: Click 'Add bootstrap action' -> Custom action -> Configure and add -> 
            Put the following in 'S3 location': s3://mda2014/rtree.sh
        * Cluster Auto-terminate: No
        
4. To run script: Add the following streaming step to your cluster with the following information:

        Replace mda2014 with your bucket name,
        * Mapper: s3://mda2014/3-pickup-patterns/mapper1.py
        * Reducer: s3://mda2014/3-pickup-patterns/reducer1.py
        * Input: s3://mda2014/taxi/trip/
        * Output: s3://mda2014/3-pickup-patterns/output1
        * Arguments: -files s3://mda2014/3-pickup-patterns/mapper2.py,s3://mda2014/3-pickup-patterns/reducer2.py,s3://mda2014/3-pickup-patterns/shapefile.py,s3://mda2014/3-pickup-patterns/tl_2013_36_tract.shp,s3://mda2014/3-pickup-patterns/tl_2013_36_tract.prj,s3://mda2014/3-pickup-patterns/tl_2013_36_tract.shp.xml,s3://mda2014/3-pickup-patterns/tl_2013_36_tract.shx,s3://mda2014/3-pickup-patterns/tl_2013_36_tract.dbf

5. Wait for finish. After the job has completed, terminate cluster.

6. To run second mapreduce, create an Amazon EMR cluster with the following configuration:
        * Termination protection: Yes
        * Logging: Enabled
        * Hadoop distribution: Amazon AMI 3.3.1
        * Cluster Auto-terminate: No

7. To run script: Add the following streaming step to your cluster with the following information:

    Replace mda2014 with your bucket name,
    * Mapper: s3://mda2014/3-pickup-patterns/mapper2.py
    * Reducer: s3://mda2014/3-pickup-patterns/reducer2.py
    * Input: s3://mda2014/3-pickup-patterns/output1/
    * Output: s3://mda2014/3-pickup-patterns/output2
    * Arguments: -files s3://mda2014/3-pickup-patterns/mapper2.py,s3://mda2014/3-pickup-patterns/reducer2.py

    Wait for finish, terminate cluster. Then download and merge all output into one file called `output.txt`

    To generate plot, execute:

        python plot_results.py output.txt <location_of_output_plot>


Author
======

[Yin Kelly]

