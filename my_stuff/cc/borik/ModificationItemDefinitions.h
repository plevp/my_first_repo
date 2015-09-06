/*!
 *  \file
 *  \author Tibor Goldschwendt (<goldschwendt@cip.ifi.lmu.de>)
 */

#ifndef CDPPLib_ModificationItemDefinitions_h
#define CDPPLib_ModificationItemDefinitions_h

#include "Definitions.h"
#include "MessageDefinitions.h"

namespace cdp { namespace cdpp {
    
    /*! \addtogroup CDP_CDPP_MODIFICATIONITEMS
     *  @{
     */
    // Types of messages.
    namespace ModificationItemType {
        
        enum ModificationItemType {
            Mesh = 0,
            Position = 1,
            Rotation = 2,
            Shape = 3,
            Parent = 4,
			Orientation = 5,
			LLAPosition = 6
        };
    }
    
    namespace ModificationItemField {
        
        // Types of modification item fields.
        typedef ModificationItemType::ModificationItemType      TypeEnum;
        typedef int                                         TypeType; 
	typedef int                                        SizeType;
        typedef OperationType::OperationType                    OperationTypeEnum;
        typedef int                                        OperationTypeType;
        typedef int                                        PolygonNumberType;
        typedef int                                         VertexNumberType;
        typedef float                                           VertexFieldType;
        typedef float                                           AngleType;
        
        // Size of message fields in bytes.
        static const size_t TypeSize                        = sizeof(TypeType);
		static const size_t SizeSize                        = sizeof(SizeType);
        static const size_t OperationTypeSize               = sizeof(OperationTypeType);
        static const size_t PolygonNumberSize               = sizeof(PolygonNumberType);
        static const size_t VertexNumberSize                = sizeof(VertexNumberType);
        static const size_t VertexFieldSize                 = sizeof(VertexFieldType);
        static const size_t AnglySize                       = sizeof(AngleType);
    }
    /*! @} */
    
} } // cdp::cdpp

#endif
