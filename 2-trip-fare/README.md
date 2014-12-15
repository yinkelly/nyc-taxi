NYC Taxi Analysis
========

Scripts to analyze taxi data on Amazon AWS: Driver's behavior

Instruction
-----------

1. Upload taxi trip and fare data to an S3 bucket. For example:
    *  s3://mda2014/taxi/trip-and-fare

2. Clone this repository and upload the scripts to your bucket on S3. For example:

    * s3://mda2014/2-trip-fare

3. To run first mapreduce job, create an Amazon EMR cluster with the following configuration:

        * Termination protection: Yes
        * Logging: Enabled
        * Hadoop distribution: Amazon AMI 3.3.1
        * Cluster Auto-terminate: No
        
4. To run script: Add the following streaming step to your cluster with the following information:

        Replace mda2014 with your bucket name,
        * Mapper: s3://mda2014/2-trip-fare/mapper1.py
        * Reducer: s3://mda2014/2-trip-fare/reducer1.py
        * Input: s3://mda2014/taxi/trip-and-fare/
        * Output: s3://mda2014/2-trip-fare/output1
        * Arguments: -files s3://mda2014/2-trip-fare/mapper1.py,s3://mda2014/2-trip-fare/reducer1.py

5. Wait for finish. After the job has completed, terminate cluster.

6. To run second mapreduce, create an Amazon EMR cluster with the following configuration:
        * Termination protection: Yes
        * Logging: Enabled
        * Hadoop distribution: Amazon AMI 3.3.1
        * Cluster Auto-terminate: No

7. To run script: Add the following streaming step to your cluster with the following information:

        Replace mda2014 with your bucket name,
        * Mapper: s3://mda2014/2-trip-fare/mapper2.py
        * Reducer: s3://mda2014/2-trip-fare/reducer2.py
        * Input: s3://mda2014/2-trip-fare/output1/
        * Output: s3://mda2014/2-trip-fare/output2
        * Arguments: -files s3://mda2014/2-trip-fare/mapper2.py,s3://mda2014/2-trip-fare/reducer2.py

    Wait for finish, terminate cluster. Then download and merge all output into one file called `output.txt`

    To generate plot, execute:

        python plot_results.py output.txt <location_of_output_plot>


Author
======

[Yin Kelly]

