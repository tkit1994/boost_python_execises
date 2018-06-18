#include <boost/python.hpp>

template <typename Dtype> Dtype fnb(Dtype n) {

  if (n <= 2)
    return 1;
  else
    return fnb(n - 1) + fnb(n - 2);
}

BOOST_PYTHON_MODULE(fnb){
    boost::python::def("fnb", fnb<long long>);
}

