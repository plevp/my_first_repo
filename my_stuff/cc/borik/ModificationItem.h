
#ifndef CDP_CDPP_MODIFICATIONITEM
#define CDP_CDPP_MODIFICATIONITEM

#include <typeinfo>


//#include "CDPPLib/Serialisers/Serialisers.h"
//#include "CDPPLib/Buffers/Buffers.h"
#include "ModificationItemDefinitions.h"
//#include "CDPPLib/Serialisers/SerDes.h"

#include "Serialisable.h"

namespace cdp { namespace cdpp {
    
    /* ! \defgroup CDP_CDPP_MODIFICATIONITEMS ModificationItems
     *  \ingroup CDP_CDPP_MESSAGES
     *  @{
     */

class ModificationItem : public Serialisable {
    
    protected:
        struct Core {
            ModificationItemField::TypeEnum             type;
            ModificationItemField::SizeType             size;
            ModificationItemField::OperationTypeEnum    operationType;
        };
        
    private:
        Core _core;
        
    protected:
        const Core& core;
        
    public:
        ModificationItem ();
        //explicit ModificationItem (Deserialiser& serialisation);
        
        virtual void serialise (SerDes& serDes); // Serialises message to byte sequence.
        
        // Getter/Setter
        virtual ModificationItemField::TypeEnum getType () const = 0;
        virtual size_t getSize () const;
        ModificationItemField::OperationTypeEnum getOperationType () const;
    };
    
    // typedef boost::shared_ptr<ModificationItem> ModificationItemPtr;
    /*! @} */
} } // cdp::cdpp

#endif /* defined(CDP_CDPP_MODIFICATIONITEM) */
