from .algorithms.shor import QFShor


class JobStatus(object):
    def __init__(self, status="", details=""):
        self.status = status if status else "ERROR"
        self.details = (
            details
            if details
            else "Job is failed or incomplete. Please try again later."
        )


class JobResponse(object):
    def __init__(
        self,
        providerJobId: str = "",
        jobStatus: JobStatus = None,
        backend={},
        jobResult={},
    ):
        self.providerJobId = providerJobId if providerJobId else ""
        self.jobStatus = jobStatus if jobStatus else JobStatus()
        self.backend = backend if backend else {"name": "UNKNOWN"}
        self.jobResult = jobResult if jobResult else {}


class Utils:
    def __init__(self):
        pass

    def generate_response(jobResponse: JobResponse) -> dict:
        if jobResponse:
            statusCode = 201  # not yet finished
            if jobResponse.jobStatus.status == "DONE":
                statusCode = 200
            jobResponse.jobStatus = vars(jobResponse.jobStatus)
            jobResponse = vars(jobResponse)  # Object to directory
            response = {"statusCode": statusCode, "body": jobResponse}
        else:
            response = {
                "statusCode": 500,
                "body": "Error in function code. Please contact the developer.",
            }
        return response

    def generate_dict_output(data, details) -> dict:
        output = {"data": data, "details": details}
        return output

    def qrng_counts_post_process(job) -> JobResponse:
        # If input type = JobResponse or have jobRawResult
        jobRawResult = {}
        if type(job) is JobResponse:
            if job.jobResult:
                jobRawResult = job.jobResult
        elif hasattr(
            job, "jobRawResult"
        ):  # Type is FunctionInvocationSchema (post-process only)
            jobRawResult = job.jobRawResult
            job = JobResponse()
        else:
            job = JobResponse()
            return job

        if jobRawResult:
            job.jobResult = PostProcess.counts_qrng(jobRawResult)
            job.jobStatus = JobStatus("DONE", "Job post processing completed")
        return job

    # General Post processing selector (type="qrng", "shor")
    def qfaas_post_process(job, ptype, requestData) -> JobResponse:
        # If input type = JobResponse or have jobRawResult
        jobRawResult = {}
        if type(job) is JobResponse:
            if job.jobResult:
                jobRawResult = job.jobResult
        elif hasattr(
            job, "jobRawResult"
        ):  # Type is FunctionInvocationSchema (post-process only)
            jobRawResult = job.jobRawResult
            job = JobResponse()
        else:
            job = JobResponse()
            return job

        if jobRawResult:
            if ptype == "qrng":
                job.jobResult = PostProcess.counts_qrng(jobRawResult)
            elif ptype == "shor":
                # Get input number
                inputNumber = requestData.input
                aShor = 2  # Default a = 2
                job.jobResult = PostProcess.shor_postprocess(
                    jobRawResult, inputNumber, aShor=2  # Default a = 2
                )
            job.jobStatus = JobStatus("DONE", "Job post processing completed")
        return job


# Post-Processing functions
class PostProcess:
    def __init__(self):
        pass

    def counts_qrng(jobCounts: dict) -> dict:
        result = max(jobCounts, key=jobCounts.get)
        occurrence = max(jobCounts.values())
        allPossibleValues = {
            k: int(k, 2) for k, v in jobCounts.items() if v == occurrence
        }
        details = {
            "decimalValue": int(result, 2),
            "numberOfOccurence": occurrence,
            "allPossibleValues": allPossibleValues,
        }
        jobResult = {"data": result, "details": details}
        return jobResult

    def shor_postprocess(counts: dict, inputNumber: int, aShor: int = 2):
        qfshor = QFShor()
        for measurement in list(counts.keys()):
            # Get the x_final value from the final state qubits
            factors = qfshor.get_factors(inputNumber, aShor, measurement)

            if factors:
                # logger.info("Found factors %s from measurement %s.", factors, measurement)
                qfshor.successful_counts = qfshor.successful_counts + 1
                if factors not in qfshor.factors:
                    qfshor.factors.append(factors)
        result = qfshor.factors
        details = {"all_counts": counts, "successful_counts": qfshor.successful_counts}
        jobResult = {"data": result, "details": details}
        return jobResult
