if __name__ == '__main__':
    from PyCoGAPS import *
    import pickle
    print("This vignette was built using pycogaps version", getVersion())

    # GET THE DATA FILE FROM A COMMAND LINE ARGUMENT
    args = sys.argv[1:]
    path = args[0]
    outFileName = args[1]

    print("Running against data file at ", path)

    # path = "data/GIST.csv"
    
    params = CoParams(path)

    setParams(params, {
        'nIterations': 500,
        'seed': 42,
        'nPatterns': 10,
        'useSparseOptimization': True,
        'distributed': "genome-wide",
    })

    print("================= START =======================")
    start = time.time()
    params.setDistributedParams(nSets=10, minNS=8, maxNS=23)
    result = CoGAPS(path, params)

    print("================= END =======================")
    end = time.time()
    print("TIME:", end - start)
            
    print("Pickling to ...", outFileName)
    pickle.dump(result, open(outFileName, "wb"))
    print("Pickling complete!")
 
