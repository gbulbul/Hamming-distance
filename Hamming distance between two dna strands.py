class find_distance:
      def ham_dist_fun(s1,s2):
          return sum(c1!=c2 for c1,c2 in zip(s1,s2))
        
if __name__ == "__main__":
    seq11='GAGCCTACTAACGGGAT'
    seq21='CATCGTAATGACGGCCT'

    print(find_distance.ham_dist_fun(seq21,seq11))
           
        
