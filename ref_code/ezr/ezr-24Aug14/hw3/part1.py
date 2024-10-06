import sys,random,os

#parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.insert(0, '/workspaces/ezr') # add parent_dir to sys.path

from ezr import the, DATA, csv, dot
import stats

def guess(N, data):
    # Pick N rows at random
    some = random.sample(data.rows, N)
    
    # Clone the data and add the picked rows, then sort on Chebyshev distance
    sorted_rows = data.clone().adds(some).chebyshevs()

    # print(sorted_rows)

    # print(type(data))
    # print(data.clone(some).cols)
    # print(data.cols)
    # assert 0
    # print(data.clone(some).chebyshev( sorted_rows[1] ))
    # print(data.clone(some).chebyshev( sorted_rows[2] ))
    # assert 0

    # Return the sorted rows
    return sorted_rows




if __name__ == '__main__':

    data_list = [arg for arg in sys.argv if arg[-4:] == ".csv"]
    # print(data_list)
    # assert 0
    dim_flag = 'low_dim'
    for data in data_list:
        #data_name = os.path.basename(data)

        d = DATA().adds(csv(data))
        # print(len(d.cols.x))
        # assert 0
        if len(d.cols.x) >= 6:
            dim_flag = 'high_dim'
        
        #baseline
        b4 = [d.chebyshev(row) for row in d.rows]
        somes = [stats.SOME(b4, f"asIs,{len(d.rows)}")]

        for N in [20,30,40,50]:
            #result_dumb  = stats.SOME(txt=f"{data_name[:-4]}_dumb_{N}")
            #result_smart  = stats.SOME(txt=f"{data_name[:-4]}_smart_{N}")
            result_dumb  = stats.SOME(txt=f"dumb_{dim_flag},{N}")
            result_smart  = stats.SOME(txt=f"smart_{dim_flag},{N}")
            somes += [result_dumb]
            somes += [result_smart]
            
            
            dumb = [guess(N,d) for _ in range(20)]
            # print(dumb)
            # for lst in dumb:
                
            #     print(d.chebyshev( lst[0] ))
            #     print(d.chebyshev( lst[1] ))
            #     print(d.chebyshev( lst[2] ))
            #     assert 0
            #print(dumb[0][0])
            dumb = [d.chebyshev( lst.rows[0] ) for lst in dumb]
            #result_dumb.add(dumb)
            
            for result in dumb:
                result_dumb.add(result)

            # smart
            the.Last = N
            smart = [d.shuffle().activeLearning() for _ in range(20) ]
            #print('!!!!!!!!!!!!!!!')
            #print(d.shuffle().activeLearning())
            #print(smart[0][0])

            smart = [d.chebyshev( lst[0] ) for lst in smart]

            for result in smart:
                result_smart.add(result)

    stats.report(somes, 0.01)        













