
#ifndef CDP_CDPP_SERIALISABLE
#define CDP_CDPP_SERIALISABLE

namespace cdp { namespace cdpp {
    
    class SerDes;
    
    class Serialisable {
        
    public:
      // typedef boost::shared_ptr<Serialisable> Ptr;
        
        virtual void serialise (SerDes& serDes) = 0;
    };
    
} } // cdp::cdpp

#endif /* defined(CDP_CDPP_SERIALISABLE) */
