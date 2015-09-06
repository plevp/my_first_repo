
#ifndef CDPPLib_Definitions_h
#define CDPPLib_Definitions_h

#include <stdlib.h>
#include <stdint.h>
#include <iostrem> 

#include "MessageDefinitions.h"

//#include "Messages/SceneMessages/ModificationItems/ModificationItem.h"

namespace cdp { namespace cdpp {

	extern const char* moduleName;
    
    // Type of object beeing updated by scene message.
    namespace ObjectType {
        
        enum ObjectType {
            Object           = 0,
            UserPosition     = 1,
            VectorShape		 = 2,
			CAVEUser		 = 3,
            OBJECTTYPE_ITEMS_COUNT
        };
    }
    
    // Type of operation applied by scene message.
    namespace OperationType {
        
        enum OperationType {
            Add             = 0,
            Delete          = 1,
            Change          = 2
        };
    }
    
    namespace MessageField {
        
        // Types of message fields.
        typedef MessageType::MessageType        TypeEnum;
        typedef int                         TypeType;
        typedef int                        SizeType;
        typedef int                        UpdateNumberType;
        typedef uint64_t                        SequenceNumberType;
        typedef uint64_t                        PluginIDType;
        typedef ObjectType::ObjectType          ObjectTypeEnum;
        typedef uint8_t                         ObjectTypeType;
        typedef uint64_t                        ObjectIDType;
        typedef OperationType::OperationType    OperationTypeEnum;
        typedef uint8_t                         OperationTypeType;
        typedef uint64_t                        ModificationItemsNumberType;
        
        // Size of message fields in bytes.
        static const size_t TypeSize                        = sizeof(TypeType);
        static const size_t SizeSize                        = sizeof(SizeType);
        static const size_t UpdateNumberSize                = sizeof(UpdateNumberType);
        static const size_t SequenceNumberSize              = sizeof(SequenceNumberType);
        static const size_t PluginIDSize                    = sizeof(PluginIDType);
        static const size_t ObjectTypeSize                  = sizeof(ObjectTypeType);
        static const size_t ObjectIDSize                    = sizeof(ObjectIDType);
        static const size_t OperationTypeSize               = sizeof(OperationTypeType);
        static const size_t ModificationItemsNumberSize     = sizeof(ModificationItemsNumberType);
    }
    
} } // cdp::cdpp

#endif
