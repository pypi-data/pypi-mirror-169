from multiprocessing import Process, JoinableQueue
import uuid
import os
import glob
import logging
import pyTigerGraph


class TgHelper:
    """TgHelper contains helper functions for use with the pyTigerGraph library

    """
    def __init__(self, conn):
        """

        Args:
            conn (TigerGraphConnection): A configured pyTigerGraph connection object
        """
        if not isinstance(conn, pyTigerGraph.TigerGraphConnection):
            raise TypeError("conn is not  a pyTigerGraph connection")
        self.conn = conn

    def execute_gsql(self, file_path):
        """Execute a gsql statement that is stored in a file

        This method reads in the gsql statement form the filepath provided and
        then executes the statement using the pyTigerGraph gsql method

        Args:
            file_path (str): Path to the file that contains the gsql statement

        Returns:
            The output received from the Tigergraph instance
        """
        with open(file_path, "r") as text_file:
            gsql_txt = text_file.read()
        _result = self.conn.gsql(gsql_txt)
        return _result
    
    def upload_job(self, source_file, job, job_filename, lines_per_file=1000000, 
                no_workers=5,timeout = 500000):
        """Uses multiprocessing to upload the file and then executes the loading job for the file

        This method splits the files into many files and then uses multiprocessing to
        individually upload and execute the loading job for each file.
        It uses the TgUpload class to perform these actions.

        Args:
            source_file (str): Path to the source file containing the data for upload
            job (str): Name of the loading job on the Tigergraph instance
            job_filename (str): Name of the file specified in the loading job
            lines_per_file (int): Number of lines per file
            no_workers (int): Number of parallel workers used for multiprocessing
            timeout (int): Timeout setting per loading job

        Returns:

        """
        _tg_upload = TgUpload(source_file, self.conn, job, job_filename, 
                lines_per_file, no_workers, timeout)
        _tg_upload.run()
    

class TgUpload:
    """This class handles the multiprocessing, file splitting, uploading and loading job execution.

    This class facilitates the execution of pyTigergraph's runLoadingJobWithFile method using
    multiproccesing

    """
    def __init__(self, source_file, tg_conn, job, job_filename, lines_per_file=1000000, no_workers=5,
                timeout = 500000):
        """

        Args:
            source_file (str): Path to the source file containing the data for upload
            tg_conn (TigerGraphConnection): A configured pyTigerGraph connection object
            job (str): Name of the loading job on the Tigergraph instance
            job_filename (str): Name of the file specified in the loading job
            lines_per_file (int): Number of lines per file
            no_workers (int): Number of parallel workers used for multiprocessing
            timeout (int): Timeout setting per loading job
        """
        self.source_file = source_file
        self.lines_per_file = lines_per_file
        self.conn = tg_conn
        self.no_workers = no_workers
        self.q = JoinableQueue()
        self.job = job
        self.timeout = timeout
        self.job_filename = job_filename
        self.producers = []
        self.directory = str(uuid.uuid4())

    def producer(self):
        """The producer splits the files and creates entries into the queue for the workers

        Returns:

        """
        if not os.path.exists(self.directory):
            os.mkdir(self.directory)
        smallfile = None
        with open(self.source_file) as bigfile:
            for lineno, line in enumerate(bigfile):
                if lineno % self.lines_per_file == 0:
                    if smallfile:
                        smallfile.close()
                        self.q.put(small_filename)
                    small_filename = '{dir}/small_file_{source_file}_{lno}.csv'.format(
                        lno=lineno + self.lines_per_file,source_file=self.source_file,
                        dir=self.directory)
                    smallfile = open(small_filename, "w")
                smallfile.write(line)
            if smallfile:
                smallfile.close()
                self.q.put(small_filename)
        pid = os.getpid()
        logging.info(f'producer {pid} done')

    def worker(self):
        """The worker fetches the next file from the queue and execute the loading job

        Returns:

        """
        while True:
            item = self.q.get()
            pid = os.getpid()
            logging.debug(f'pid {pid} Working on {item}')
            self.conn.runLoadingJobWithFile(item, self.job_filename, self.job,
                                            timeout=self.timeout, sizeLimit = 128000000)
            os.remove(f"{item}")
            logging.debug(f'pid {pid} Finished {item}')
            self.q.task_done()
            
    def start_workers(self):
        """Start the number of specified workers

        Returns:

        """
        for i in range(self.no_workers):
            Process(target=self.worker, daemon=True).start()
    
    def start_producers(self):
        """Start a single producer

        Returns:

        """
        for i in range(1):
            p = Process(target=self.producer)
            self.producers.append(p)
            p.start()
            # make sure producers done
            for p in self.producers:
                p.join()

    def run(self):
        """Execute the process of starting workers and producers and waiting for them to finish

        Returns:

        """
        self.start_workers()
        self.start_producers()
        self.q.join()
        logging.info('All work completed')


    