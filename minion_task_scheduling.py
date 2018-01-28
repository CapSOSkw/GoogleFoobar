def answer(data, n):
    # your code here
    count_jobs_dict = ((i, data.count(i)) for i in data)

#     job_index = [i[0] for i in count_jobs_dict]
#     job_count = [i[1] for i in count_jobs_dict]
    # max_count = max(job_count)
    
    job_index, job_count = [], []

    for i in count_jobs_dict:
        job_index.append(i[0])
        job_count.append(i[1])
    
    max_count = -1
    for i in job_count:
        if i > max_count:
            max_count = i

    if n == 0:
        return []

    result = []
    for i, j in enumerate(job_count):
        if j <= n:
            result.append(job_index[i])

    return result


print(answer([5,10,15,10,7], 1))
