Step 1  Downloading Sqoop https://sqoop.apache.org/

        We can download the latest version of Sqoop from the following link For this tutorial, we are using version 1.4.5, that is, sqoop-1.4.5.bin__hadoop-2.0.4-alpha.tar.gz.

Step 2: Installing Sqoop

    The following commands are used to extract the Sqoop tar ball and move it to “/usr/lib/sqoop” directory.

    >> tar -xvf sqoop-1.4.4.bin__hadoop-2.0.4-alpha.tar.gz

    >>  mv sqoop-1.4.4.bin__hadoop-2.0.4-alpha /usr/lib/sqoop

Step 5: Configuring bashrc

    You have to set up the Sqoop environment by appending the following lines to ~/.bashrc file −

    #Sqoop
    export SQOOP_HOME=/usr/lib/sqoop 
    export PATH=$PATH:$SQOOP_HOME/bin

    The following command is used to execute ~/.bashrc file.

    >> source ~/.bashrc

Step 6: Configuring Sqoop

        To configure Sqoop with Hadoop, you need to edit the sqoop-env.sh file, which is placed in the $SQOOP_HOME/conf directory. First of all, Redirect to Sqoop config directory and copy the template file using the following command −

        >> cd $SQOOP_HOME/conf
        >> mv sqoop-env-template.sh sqoop-env.sh

        Open sqoop-env.sh and edit the following lines −

        export HADOOP_COMMON_HOME=/home/samson/hadoop-3.3.3
        export HADOOP_MAPRED_HOME=/home/samson/hadoop-3.3.3

Step 7: Download and Configure mysql-connector-java

        We can download mysql-connector-java-5.1.30.tar.gz file from the following link http://ftp.ntu.edu.tw/MySQL/Downloads/Connector-J/

        The following commands are used to extract mysql-connector-java tarball and move mysql-connector-java-5.1.30-bin.jar to /usr/lib/sqoop/lib directory.

        $ tar -zxf mysql-connector-java-5.1.30.tar.gz
        $ su
        password:

        Move JDBC drive to the lib location accessible by Sqoop
        # cd mysql-connector-java-5.1.30
        # mv mysql-connector-java-5.1.30-bin.jar /usr/lib/sqoop/lib

Step 8: Verifying Sqoop

        The following command is used to verify the Sqoop version.

        $ cd $SQOOP_HOME/bin
        $ sqoop-version


See Sqoop command

=======
Ensure
=======

- Common Lanaguage 2.6  is added usr/lib/sqoop/lib  => Download from here https://mvnrepository.com/artifact/commons-lang/commons-lang/2.6 
- mapred-site.xml is updated base on the file


Setup s3 file migration with sqoop
=================================