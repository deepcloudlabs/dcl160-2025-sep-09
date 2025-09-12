with open("employees.txt",mode="rt") as file:
    try:
        for line in file:
            full_name,department,salary,birth_year,full_time=line.split(",")
            print(type(salary))
            salary = float(salary.strip())
            birth_year = int(birth_year.strip())
            full_time = full_time.strip().capitalize() == "True"
            print(f"{full_name},{department},{salary},{birth_year},{full_time}")
    except IOError as e:
        print(e)