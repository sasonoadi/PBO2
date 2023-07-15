t = b"a".decode("ascii")
  
# Produces error
t1 = b"a\xf1".decode("ascii")