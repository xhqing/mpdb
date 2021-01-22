import multiprocessing
  
def child_process():
    
    import mpdb
    mpdb.set_trace()
    var = "debug me child!"
    a = 2
    b = 3
    if b > a:
        c = b - a
    
  
def main_process():
   
    p = multiprocessing.Process(target=child_process)
    p.start()
    var = "debug me main"
    a = 3
    b = 4
    c = 6
    p.join()
  
if __name__ == "__main__":
    main_process()
