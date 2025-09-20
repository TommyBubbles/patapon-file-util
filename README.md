# TODO:
## - make the file header available to all classes within the main class
## - combine PataponStaticDataClass and PataponDynamicDataClass into one class (PataponDataClass)
##   * implement the to_bytes logic for dynamic data and format_string (potentially factor out instead)
## - speed up files processing
##   * use a file instead of raw bytes to help with read speed (mmap, fileinput, open)
##   * use multiprocessing for lists of PataponDataClasses
## - implement reading zip files and bnd files
##   * bnd partitioning logic is still needed
##     x mostly done, still need to work on different file type processing

# Notes:
## - CharaBirthParam does not capture all of the AdjustDamageParams due to the count for it
##   being off (by 4) in the original file. original count: 0x5D, actual count: 0x61


# patapon-file-util
## data file checklist (Patapon 1):
### actor folder
#### actor folder
##### unit data
##### - model.amdl
##### - model.amdl/\*.gxx
##### - localdata.bnd
##### - localdata.bnd/equipmodel.amdl
##### - localdata.bnd/equipmodel.amdl/\*.gxx
##### - localdata.bnd/model.amdl
##### - localdata.bnd/model.amdl/\*.gxx
##### - localdata.bnd/model.amdl/\*.gxt
##### - localdata.bnd/charaparam.dat -> CharaParam
##### - localdata.bnd/defaultequiplist.bnd
##### - localdata.bnd/defaultequiplist.bnd/unit\*.dat -> NodeName
##### - localdata.bnd/nodenamelist.bnd
##### - localdata.bnd/nodenamelist.bnd/unit\*.dat -> NodeName
##### - actorparam.dat -> ActorParam
##### - collisionparamlist.bnd
##### - collisionparamlist.bnd/unit\*.dat -> CollisionParam


#### equip folder
##### equip data
##### - equipparam.dat -> EquipParam
##### - model.amdl
##### - model.amdl/\*.gxx
##### - model.amdl/\*.gxt
##### - actorparam.dat -> ActorParam
##### - modenamelist.bnd
##### - modenamelist.bnd/unit\*.dat -> NodeName


#### mission folder
##### mission data
##### - mission.bnd
##### - mission.bnd/missionparam.dat -> MissionParam
##### - mission.bnd/missionscript.pac
##### - mission.bnd/stagescript.pac
##### - mission.bnd/missionmessage.lbnd
##### - mission.bnd/missionmessage.lbnd/\*.bnd
##### - mission.bnd/missionmessage.lbnd/\*.bnd/mission.pac
##### - mission.bnd/bgm.dat
##### - mission.bnd/bgm.dat/\*.sgd
##### - mission.bnd/bgm.dat/\*.lrt
##### - mission.bnd/bgm.dat/param.dat -> BGMParam

##### - predata.bnd
##### - predata.bnd/missionmessage.lbnd
##### - predata.bnd/missionmessage.lbnd/\*.bnd
##### - predata.bnd/missionmessage.lbnd/\*.bnd/mission.pac
##### - predata.bnd/missionparam.dat -> MissionParam

##### - stagedata.bnd
##### - stagedata.bnd/stage.bns
##### - stagedata.bnd/stage.bns/unknown_0.bnd -> StageAreaParam
##### - stagedata.bnd/stage.bns/unknown_1.bnd -> StageGimmickParam
##### - stagedata.bnd/stage.bns/unknown_2.bnd
##### - stagedata.bnd/stage.bns/unknown_2.bnd/\*.gxx
##### - stagedata.bnd/stage.bns/unknown_3.bnd
##### - stagedata.bnd/stage.bns/unknown_3.bnd/\*.gxt
##### - stagedata.bnd/stage.bns/unknown_4.bnd
##### - stagedata.bnd/stage.bns/unknown_4.bnd/\*.sgd

##### - unitdata.bnd
##### - unitdata.bnd/unit.bnd
##### - unitdata.bnd/unit.bnd/equipdata.bnd
##### - unitdata.bnd/unit.bnd/equipdata.bnd/hlm\*.bnds
##### - unitdata.bnd/unit.bnd/equipdata.bnd/wpn\*.bnds
##### - unitdata.bnd/unit.bnd/equipdata.bnd/sld\*.bnds
##### - unitdata.bnd/unit.bnd/unitdata.bnd
##### - unitdata.bnd/unit.bnd/unitdata.bnd/unit\*.bnd


### loadinggroup
#### systemdata.bnd
#### systemdata.bnd/default.bnd
#### systemdata.bnd/default.bnd/effect.bin
#### systemdata.bnd/default.bnd/effect.bin/*.bnd
#### systemdata.bnd/default.bnd/message.nebnd
#### systemdata.bnd/default.bnd/message.nebnd/window.amdl
#### systemdata.bnd/default.bnd/message.nebnd/window.amdl/\*.gxx
#### systemdata.bnd/default.bnd/message.nebnd/window.amdl/\*.gxt
#### systemdata.bnd/default.bnd/message.nebnd/unicodetable.bnd
#### systemdata.bnd/default.bnd/message.nebnd/unicodetable.bnd/data
#### systemdata.bnd/default.bnd/message.nebnd/unicodetable.bnd/data/ucs2jis.dat
#### systemdata.bnd/default.bnd/message.nebnd/unicodetable.bnd/data/jis2ucs.dat
#### systemdata.bnd/default.bnd/sound.dat
#### systemdata.bnd/default.bnd/sound.dat/\*.sgd
#### systemdata.bnd/default.bnd/sound.dat/\*.gxx
#### systemdata.bnd/default.bnd/sound.dat/semixer.pac
#### systemdata.bnd/default.bnd/loadinggroupcmn.bnd


#### systemlocalizedata.bnd
#### systemlocalizedata.bnd/default.bnd
#### systemlocalizedata.bnd/default.bnd/localize.lbnd
#### systemlocalizedata.bnd/default.bnd/localize.lbnd/\*.bnd
#### systemlocalizedata.bnd/default.bnd/localize.lbnd/\*.bnd/font.bnd
#### systemlocalizedata.bnd/default.bnd/localize.lbnd/\*.bnd/font.bnd/\*.ftl
#### systemlocalizedata.bnd/default.bnd/localize.lbnd/\*.bnd/font.bnd/outlinefont.dat
#### systemlocalizedata.bnd/default.bnd/localize.lbnd/\*.bnd/font.bnd/outlinefont.dat/\*.gxt
#### systemlocalizedata.bnd/default.bnd/localize.lbnd/\*.bnd/font.bnd/systemfont.dat
#### systemlocalizedata.bnd/default.bnd/localize.lbnd/\*.bnd/font.bnd/systemfont.dat/\*.gxt
#### systemlocalizedata.bnd/default.bnd/localize.lbnd/\*.bnd/icon.bnd
#### systemlocalizedata.bnd/default.bnd/localize.lbnd/\*.bnd/icon.bnd/\*.png
#### systemlocalizedata.bnd/default.bnd/localize.lbnd/\*.bnd/scriptlist.bnd/\*.msg
#### systemlocalizedata.bnd/default.bnd/localize.lbnd/\*.bnd/scriptlist.bnd/\*.pac
#### systemlocalizedata.bnd/default.bnd/localize.lbnd/\*.bnd/localizedtexl.texls
#### systemlocalizedata.bnd/default.bnd/localize.lbnd/\*.bnd/localizedtexl.texls/\*.gxt


#### titledata.bnd
#### titledata.bnd/default.bnd
#### titledata.bnd/default.bnd/sound.dat
#### titledata.bnd/default.bnd/sound.dat/\*.sgd
#### titledata.bnd/default.bnd/loadinggroupcmn.bnd -> loadinggroupcmn
#### titledata.bnd/default.bnd/localize.lbnd
#### titledata.bnd/default.bnd/localize.lbnd/\*.bnd
#### titledata.bnd/default.bnd/localize.lbnd/\*.bnd/localizemodell.mdll
#### titledata.bnd/default.bnd/localize.lbnd/\*.bnd/localizemodell.mdll/\*.gxx
#### titledata.bnd/default.bnd/localize.lbnd/\*.bnd/localizemodell.mdll/\*.gxt
#### titledata.bnd/default.bnd/localize.lbnd/\*.bnd/scriptlist
#### titledata.bnd/default.bnd/localize.lbnd/\*.bnd/scriptlist/\*.msg


#### logodata.bnd
#### logodata.bnd/default.bnd
#### logodata.bnd/default.bnd/localize.lbnd
#### logodata.bnd/default.bnd/localize.lbnd/\*.bnd
#### logodata.bnd/default.bnd/localize.lbnd/\*.bnd/localizemodell.mdll
#### logodata.bnd/default.bnd/localize.lbnd/\*.bnd/localizemodell.mdll\*.gxt
#### logodata.bnd/default.bnd/localize.lbnd/\*.bnd/localizemodell.mdll\*.gxx


#### gamedata.bnd
#### gamedata.bnd/default.bnd
#### gamedata.bnd/default.bnd/windpath.bns
#### gamedata.bnd/default.bnd/windpath.bns/
#### gamedata.bnd/default.bnd/loadinggroupcmn.bnd -> loadinggroupcmn


#### basesdata.bnd
#### basesdata.bnd/default.bnd/
#### basesdata.bnd/default.bnd/stage.bnd -> stage.bns
#### basesdata.bnd/default.bnd/camp_event.pac
#### basesdata.bnd/default.bnd/camppartstex.bnd
#### basesdata.bnd/default.bnd/camppartstex.bnd/\*.gxt
#### basesdata.bnd/default.bnd/camppartsmodel.bnd
#### basesdata.bnd/default.bnd/camppartsmodel.bnd/hlm\*.bnd
#### basesdata.bnd/default.bnd/camppartsmodel.bnd/chr\*.bnd
#### basesdata.bnd/default.bnd/camppartsmodel.bnd/sld\*.bnd
#### basesdata.bnd/default.bnd/camppartsmodel.bnd/wpn\*.bnd
#### basesdata.bnd/default.bnd/camppartsmodel.bnd/opt\*.bnd
#### basesdata.bnd/default.bnd/camppartsmodel.bnd/cln_ui\*.bnd
#### basesdata.bnd/default.bnd/camppartsmodel.bnd/cln\*.bnd
#### basesdata.bnd/default.bnd/camppartsmodel.bnd/\*.bnd/\*.gxt
#### basesdata.bnd/default.bnd/camppartsmodel.bnd/\*.bnd/\*.gxx
#### basesdata.bnd/default.bnd/loadinggroupcmn.bnd -> loadinggroupcmn
#### basesdata.bnd/default.bnd/sound.bnd
#### basesdata.bnd/default.bnd/sound.bnd/\*.sgd
#### basesdata.bnd/default.bnd/sound.bnd/\*.lrt
#### basesdata.bnd/default.bnd/sound.bnd/param.dat
#### basesdata.bnd/default.bnd/worldmap.bnd
#### basesdata.bnd/default.bnd/worldmap.bnd/flash.bnd
#### basesdata.bnd/default.bnd/worldmap.bnd/flash.bnd/wm_\*.bnd
#### basesdata.bnd/default.bnd/worldmap.bnd/flash.bnd/wm_\*.bnd/TWS?
#### basesdata.bnd/default.bnd/worldmap.bnd/flash.bnd/wm_\*.bnd/unknown_1.bnd
#### basesdata.bnd/default.bnd/worldmap.bnd/flash.bnd/wm_\*.bnd/unknown_1.bnd/\*.gxt
#### basesdata.bnd/default.bnd/worldmap.bnd/texturelist.bnd
#### basesdata.bnd/default.bnd/worldmap.bnd/texturelist.bnd/worldmap.texl
#### basesdata.bnd/default.bnd/worldmap.bnd/texturelist.bnd/worldmap.texl/\*.gxt


#### organizationdata.bnd
#### organizationdata.bnd/default.bnd
#### organizationdata.bnd/default.bnd/loadinggroupcmn.bnd -> loadinggroupcmn


### loadinggroupcmn
#### loadinggroupcmn/actorresourcenode.bnd
#### loadinggroupcmn/actorresourcenode.bnd/\*.arc -> Unit
#### loadinggroupcmn/actorresourcenode.bnd/unit\*.bnd -> Unit

#### loadinggroupcmn/layoutlist.layl
#### loadinggroupcmn/layoutlist.layl/scenelayoutparam\*.dat

#### loadinggroupcmn/modellist.bnd
#### loadinggroupcmn/modellist.bnd/loading.mdll
#### loadinggroupcmn/modellist.bnd/loading.mdll/\*.gxx
#### loadinggroupcmn/modellist.bnd/loading.mdll/\*.gxt
#### loadinggroupcmn/modellist.bnd/system.mdll
#### loadinggroupcmn/modellist.bnd/camp.mdll
#### loadinggroupcmn/modellist.bnd/camp.mdll/\*.gxx
#### loadinggroupcmn/modellist.bnd/game.mdll
#### loadinggroupcmn/modellist.bnd/game.mdll/\*.gxx
#### loadinggroupcmn/modellist.bnd/game.mdll/\*.gxt
#### loadinggroupcmn/modellist.bnd/organization.mdll
#### loadinggroupcmn/modellist.bnd/organization.mdll/\*.gxx
#### loadinggroupcmn/modellist.bnd/organization.mdll/\*.gxt

#### loadinggroupcmn/paramlist.bnd
#### loadinggroupcmn/paramlist.bnd/abnormalstatusparam.dat -> AbnormalStatusParam
#### loadinggroupcmn/paramlist.bnd/carnivalpowerevalutateparam.dat -> CarnivalPowerEvalutateParam
#### loadinggroupcmn/paramlist.bnd/carnivalpowerevalutateparambases.dat -> CarnivalPowerEvalutateParamBases
#### loadinggroupcmn/paramlist.bnd/charabirthparam.dat -> CharaBirthParam
#### loadinggroupcmn/paramlist.bnd/charagroupparam.dat -> CharaGroupParam
#### loadinggroupcmn/paramlist.bnd/cookingparam.dat -> CookingParam
#### loadinggroupcmn/paramlist.bnd/effectparam.dat -> EffectParam
#### loadinggroupcmn/paramlist.bnd/gameparam.dat -> GameParam
#### loadinggroupcmn/paramlist.bnd/hiteffecttableparam.dat -> HitEffectTableParam
#### loadinggroupcmn/paramlist.bnd/instructioncommandparam.dat -> InstructionCommandParam
#### loadinggroupcmn/paramlist.bnd/laboparam.dat -> LaboParam
#### loadinggroupcmn/paramlist.bnd/miracleparam.dat -> MiracleParam
#### loadinggroupcmn/paramlist.bnd/missionparam.dat -> SystemDataMissionParam
#### loadinggroupcmn/paramlist.bnd/particleparam.dat -> ParticleParam 
#### loadinggroupcmn/paramlist.bnd/soundgameparam.dat -> SoundGameParam
#### loadinggroupcmn/paramlist.bnd/soundparam.dat -> SoundParam
#### loadinggroupcmn/paramlist.bnd/squadlineparam.dat -> SquadLineParam
#### loadinggroupcmn/paramlist.bnd/systemparam.dat -> SystemParam
#### loadinggroupcmn/paramlist.bnd/charaparam.dat -> BasesDataCharaParam
#### loadinggroupcmn/paramlist.bnd/facilityparam.dat -> FacilityPersonParam
#### loadinggroupcmn/paramlist.bnd/nodenameparam.dat -> NodeNameParam
#### loadinggroupcmn/paramlist.bnd/personparam.dat -> FacilityPersonParam
#### loadinggroupcmn/paramlist.bnd/weaponparam.dat -> WeaponEquipParam
#### loadinggroupcmn/paramlist.bnd/motiontimingparam.dat -> MotionTimingParam
#### loadinggroupcmn/paramlist.bnd/motiontypeparam.dat -> MotionTypeParam
#### loadinggroupcmn/paramlist.bnd/squadactivityparam.dat -> SquadActivityParam
#### loadinggroupcmn/paramlist.bnd/squadcrtlfuncparam.dat -> SquadCtrlFuncParam
#### loadinggroupcmn/paramlist.bnd/unitlayoutparam_e.dat -> UnitLayoutParamE
#### loadinggroupcmn/scriptlist.bnd
#### loadinggroupcmn/scriptlist.bnd/effect.pac
#### loadinggroupcmn/scriptlist.bnd/itemtable.pac
#### loadinggroupcmn/scriptlist.bnd/labo.pac
#### loadinggroupcmn/scriptlist.bnd/system.pac
#### loadinggroupcmn/scriptlist.bnd/actor.pac
#### loadinggroupcmn/scriptlist.bnd/camp_event.pac -> Stage PAC
#### loadinggroupcmn/scriptlist.bnd/colony_data.pac -> PAC
#### loadinggroupcmn/scriptlist.bnd/gamemain.pac -> PAC
#### loadinggroupcmn/scriptlist.bnd/gamemodule.pac -> PAC
#### loadinggroupcmn/scriptlist.bnd/march.pac -> PAC
#### loadinggroupcmn/scriptlist.bnd/missionmain.pac -> PAC
#### loadinggroupcmn/scriptlist.bnd/unitbase.pac -> PAC
#### loadinggroupcmn/scriptlist.bnd/unitsquad.pac -> PAC

#### loadinggroupcmn/sound.dat
#### loadinggroupcmn/sound.dat/\*.sgd


#### loadinggroupcmn/texturelist.bnd
#### loadinggroupcmn/texturelist.bnd/system.texls
#### loadinggroupcmn/texturelist.bnd/system.texls/\*.gxt
#### loadinggroupcmn/texturelist.bnd/system.texl
#### loadinggroupcmn/texturelist.bnd/system.texl/\*.gxt
#### loadinggroupcmn/texturelist.bnd/camp.bnd
#### loadinggroupcmn/texturelist.bnd/camp.bnd/\*.gxt
#### loadinggroupcmn/texturelist.bnd/game.bnd


### movie
#### \*.pmf


### sound
#### miracle_bgm_\*.bnd/\*.sgd
#### miracle_bgm_\*.bnd/\*.gxx
#### miracle_bgm_\*.bnd/\*.texls
#### miracle_bgm_\*.bnd/\*.texls/\*.gxt
#### miracle_bgm_\*.bnd/\*.lrt
#### miracle_bgm_\*.bnd/command.pac


### soundgame
#### chr\*.amdl
#### chr\*.amdl/\*.gxx
#### chr\*.amdl/\*.gxt
#### loadinggroupcmn.bnd -> loadinggroupcmn
#### sound.bin
#### sound.bin/\*.sgd
#### sound.bin/\*.lrt
#### sound.bin/command.pac


### tips
#### us/tips\*.gxt/\*.gxt