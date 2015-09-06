/*!
 *  \file
 *  \author Tibor Goldschwendt (<goldschwendt@cip.ifi.lmu.de>)
 */

// #include <boost/make_shared.hpp>
#include "ModificationItem.h"

using namespace cdp::cdpp;
// using namespace boost;

ModificationItem::ModificationItem () : core(this->_core) {
    
}

void ModificationItem::serialise (SerDes& serDes) {
   
  /** LP
    if (serDes.isSerialising()) {
        this->_core.type = this->getType();
        this->_core.size = this->getSize();
    }
    serDes & SerDesPair((uint64_t&)this->_core.type, ModificationItemField::TypeSize);
    serDes & this->_core.size;
    serDes & SerDesPair((uint64_t&)this->_core.operationType, ModificationItemField::OperationTypeSize);
  **/
  this->_core.type = this->getType();
  this->_core.size = this->getSize();

}

size_t ModificationItem::getSize () const {
    return ModificationItemField::TypeSize + ModificationItemField::SizeSize + ModificationItemField::OperationTypeSize;
}

ModificationItemField::OperationTypeEnum ModificationItem::getOperationType () const {
    return this->core.operationType;
}

