# patapon-file-util
## data file checklist:
### actor folder
#### actor folder
##### unit data
##### - model.amdl
##### - model.amdl/*.gxx
##### - localdata.bnd
##### - localdata.bnd/equipmodel.amdl
##### - localdata.bnd/equipmodel.amdl/*.gxx
##### - localdata.bnd/model.amdl
##### - localdata.bnd/model.amdl/*.gxx
##### - localdata.bnd/model.amdl/*.gxt
##### - localdata.bnd/charaparam.dat -> CharaParam
##### - localdata.bnd/defaultequiplist.bnd
##### - localdata.bnd/defaultequiplist.bnd/unit*.dat -> NodeName
##### - localdata.bnd/nodenamelist.bnd
##### - localdata.bnd/nodenamelist.bnd/unit*.dat -> NodeName
##### - actorparam.dat -> ActorParam
##### - collisionparamlist.bnd
##### - collisionparamlist.bnd/unit*.dat -> CollisionParam

#### equip folder
##### equip data
##### - equipparam.dat -> EquipParam
##### - model.amdl
##### - model.amdl/*.gxx
##### - model.amdl/*.gxt
##### - actorparam.dat -> ActorParam
##### - modenamelist.bnd
##### - modenamelist.bnd/unit*.dat -> NodeName

#### mission folder
##### mission data
##### - mission.bnd
##### - mission.bnd/missionparam.dat -> MissionParam
##### - mission.bnd/missionscript.pac
##### - mission.bnd/stagescript.pac
##### - mission.bnd/missionmessage.lbnd
##### - mission.bnd/missionmessage.lbnd/cn.bnd
##### - mission.bnd/missionmessage.lbnd/cn.bnd/mission.pac
##### - mission.bnd/missionmessage.lbnd/de.bnd
##### - mission.bnd/missionmessage.lbnd/de.bnd/mission.pac
##### - mission.bnd/missionmessage.lbnd/fr.bnd
##### - mission.bnd/missionmessage.lbnd/fr.bnd/mission.pac
##### - mission.bnd/missionmessage.lbnd/it.bnd
##### - mission.bnd/missionmessage.lbnd/it.bnd/mission.pac
##### - mission.bnd/missionmessage.lbnd/jp.bnd
##### - mission.bnd/missionmessage.lbnd/jp.bnd/mission.pac
##### - mission.bnd/missionmessage.lbnd/kr.bnd
##### - mission.bnd/missionmessage.lbnd/kr.bnd/mission.pac
##### - mission.bnd/missionmessage.lbnd/sp.bnd
##### - mission.bnd/missionmessage.lbnd/sp.bnd/mission.pac
##### - mission.bnd/missionmessage.lbnd/uk.bnd
##### - mission.bnd/missionmessage.lbnd/uk.bnd/mission.pac
##### - mission.bnd/missionmessage.lbnd/us.bnd
##### - mission.bnd/missionmessage.lbnd/us.bnd/mission.pac
##### - mission.bnd/bgm.dat
##### - mission.bnd/bgm.dat/*.sgd
##### - mission.bnd/bgm.dat/*.lrt
##### - mission.bnd/bgm.dat/param.dat -> BGMParam

##### - predata.bnd
##### - predata.bnd/missionmessage.lbnd
##### - predata.bnd/missionmessage.lbnd/cn.bnd
##### - predata.bnd/missionmessage.lbnd/cn.bnd/mission.pac
##### - predata.bnd/missionmessage.lbnd/de.bnd
##### - predata.bnd/missionmessage.lbnd/de.bnd/mission.pac
##### - predata.bnd/missionmessage.lbnd/fr.bnd
##### - predata.bnd/missionmessage.lbnd/fr.bnd/mission.pac
##### - predata.bnd/missionmessage.lbnd/it.bnd
##### - predata.bnd/missionmessage.lbnd/it.bnd/mission.pac
##### - predata.bnd/missionmessage.lbnd/jp.bnd
##### - predata.bnd/missionmessage.lbnd/jp.bnd/mission.pac
##### - predata.bnd/missionmessage.lbnd/kr.bnd
##### - predata.bnd/missionmessage.lbnd/kr.bnd/mission.pac
##### - predata.bnd/missionmessage.lbnd/sp.bnd
##### - predata.bnd/missionmessage.lbnd/sp.bnd/mission.pac
##### - predata.bnd/missionmessage.lbnd/uk.bnd
##### - predata.bnd/missionmessage.lbnd/uk.bnd/mission.pac
##### - predata.bnd/missionmessage.lbnd/us.bnd
##### - predata.bnd/missionmessage.lbnd/us.bnd/mission.pac
##### - predata.bnd/missionparam.dat -> MissionParam

##### - stagedata.bnd
##### - stagedata.bnd/stage.bns
##### - stagedata.bnd/stage.bns/unknown_0.bnd -> StageAreaParam
##### - stagedata.bnd/stage.bns/unknown_1.bnd -> StageGimmickParam
##### - stagedata.bnd/stage.bns/unknown_2.bnd
##### - stagedata.bnd/stage.bns/unknown_2.bnd/*.gxx
##### - stagedata.bnd/stage.bns/unknown_3.bnd
##### - stagedata.bnd/stage.bns/unknown_3.bnd/*.gxt
##### - stagedata.bnd/stage.bns/unknown_4.bnd
##### - stagedata.bnd/stage.bns/unknown_4.bnd/*.sgd

##### - unitdata.bnd
##### - unitdata.bnd/unit.bnd
##### - unitdata.bnd/unit.bnd/equipdata.bnd
##### - unitdata.bnd/unit.bnd/equipdata.bnd/hlm*.bnds
##### - unitdata.bnd/unit.bnd/equipdata.bnd/wpn*.bnds
##### - unitdata.bnd/unit.bnd/equipdata.bnd/sld*.bnds
##### - unitdata.bnd/unit.bnd/unitdata.bnd
##### - unitdata.bnd/unit.bnd/unitdata.bnd/unit*.bnd

### loadinggroup
#### systemdata.bnd
#### systemdata.bnd/default.bnd
#### systemdata.bnd/default.bnd/effect.bin
#### systemdata.bnd/default.bnd/effect.bin/*.bnd
#### systemdata.bnd/default.bnd/message.nebnd
#### systemdata.bnd/default.bnd/message.nebnd/window.amdl
#### systemdata.bnd/default.bnd/message.nebnd/window.amdl/*.gxx
#### systemdata.bnd/default.bnd/message.nebnd/window.amdl/*.gxt
#### systemdata.bnd/default.bnd/message.nebnd/unicodetable.bnd
#### systemdata.bnd/default.bnd/message.nebnd/unicodetable.bnd/data
#### systemdata.bnd/default.bnd/message.nebnd/unicodetable.bnd/data/ucs2jis.dat
#### systemdata.bnd/default.bnd/message.nebnd/unicodetable.bnd/data/jis2ucs.dat
#### systemdata.bnd/default.bnd/sound.dat
#### systemdata.bnd/default.bnd/sound.dat/*.sgd
#### systemdata.bnd/default.bnd/sound.dat/*.gxx
#### systemdata.bnd/default.bnd/sound.dat/semixer.pac
#### systemdata.bnd/default.bnd/loadinggroupcmn
#### systemdata.bnd/default.bnd/loadinggroupcmn/actorresourcenode.bnd
#### systemdata.bnd/default.bnd/loadinggroupcmn/actorresourcenode.bnd/*.arc
#### systemdata.bnd/default.bnd/loadinggroupcmn/layoutlist.layl
#### systemdata.bnd/default.bnd/loadinggroupcmn/layoutlist.layl/scenelayoutparam*.dat
#### systemdata.bnd/default.bnd/loadinggroupcmn/modellist.bnd
#### systemdata.bnd/default.bnd/loadinggroupcmn/modellist.bnd/loading.mdll
#### systemdata.bnd/default.bnd/loadinggroupcmn/modellist.bnd/loading.mdll/*.gxx
#### systemdata.bnd/default.bnd/loadinggroupcmn/modellist.bnd/loading.mdll/*.gxt
#### systemdata.bnd/default.bnd/loadinggroupcmn/modellist.bnd/system.mdll
#### systemdata.bnd/default.bnd/loadinggroupcmn/paramlist.bnd
#### systemdata.bnd/default.bnd/loadinggroupcmn/paramlist.bnd/abnormalstatusparam.dat -> AbnormalStatusParam
#### systemdata.bnd/default.bnd/loadinggroupcmn/paramlist.bnd/carnivalpowerevalutateparam.dat
#### systemdata.bnd/default.bnd/loadinggroupcmn/paramlist.bnd/carnivalpowerevalutateparambases.dat
#### systemdata.bnd/default.bnd/loadinggroupcmn/paramlist.bnd/charabirthparam.dat
#### systemdata.bnd/default.bnd/loadinggroupcmn/paramlist.bnd/charagroupparam.dat
#### systemdata.bnd/default.bnd/loadinggroupcmn/paramlist.bnd/cookingparam.dat
#### systemdata.bnd/default.bnd/loadinggroupcmn/paramlist.bnd/effectparam.dat
#### systemdata.bnd/default.bnd/loadinggroupcmn/paramlist.bnd/gameparam.dat
#### systemdata.bnd/default.bnd/loadinggroupcmn/paramlist.bnd/hiteffecttableparam.dat
#### systemdata.bnd/default.bnd/loadinggroupcmn/paramlist.bnd/instructioncommandparam.dat
#### systemdata.bnd/default.bnd/loadinggroupcmn/paramlist.bnd/laboparam.dat
#### systemdata.bnd/default.bnd/loadinggroupcmn/paramlist.bnd/miracleparam.dat
#### systemdata.bnd/default.bnd/loadinggroupcmn/paramlist.bnd/missionparam.dat
#### systemdata.bnd/default.bnd/loadinggroupcmn/paramlist.bnd/particleparam.dat
#### systemdata.bnd/default.bnd/loadinggroupcmn/paramlist.bnd/soundgameparam.dat
#### systemdata.bnd/default.bnd/loadinggroupcmn/paramlist.bnd/soundparam.dat
#### systemdata.bnd/default.bnd/loadinggroupcmn/paramlist.bnd/squadlineparam.dat
#### systemdata.bnd/default.bnd/loadinggroupcmn/paramlist.bnd/systemparam.dat
#### systemdata.bnd/default.bnd/loadinggroupcmn/paramlist.bnd/unitparam.dat
#### systemdata.bnd/default.bnd/loadinggroupcmn/scriptlist.bnd
#### systemdata.bnd/default.bnd/loadinggroupcmn/scriptlist.bnd/effect.pac
#### systemdata.bnd/default.bnd/loadinggroupcmn/scriptlist.bnd/itemtable.pac
#### systemdata.bnd/default.bnd/loadinggroupcmn/scriptlist.bnd/labo.pac
#### systemdata.bnd/default.bnd/loadinggroupcmn/scriptlist.bnd/system.pac
#### systemdata.bnd/default.bnd/loadinggroupcmn/scriptlist.bnd/actor.pac
#### systemdata.bnd/default.bnd/loadinggroupcmn/texturelist.bnd
#### systemdata.bnd/default.bnd/loadinggroupcmn/texturelist.bnd/system.texls
#### systemdata.bnd/default.bnd/loadinggroupcmn/texturelist.bnd/system.texls/*.gxt
#### systemdata.bnd/default.bnd/loadinggroupcmn/texturelist.bnd/system.texl
#### systemdata.bnd/default.bnd/loadinggroupcmn/texturelist.bnd/system.texl/*.gxt

#### systemlocalizedata.bnd
#### titledata.bnd
#### logodata.bnd
#### gamedata.bnd
#### basesdata.bnd
#### organizationdata.bnd