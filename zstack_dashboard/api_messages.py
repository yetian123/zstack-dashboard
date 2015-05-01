api_names = [
    'org.zstack.test.multinodes.APISilentMsg',
    'org.zstack.test.identity.FakePolicyAllowMsg',
    'org.zstack.test.identity.FakePolicyDenyMsg',
    'org.zstack.test.identity.FakePolicyAllowHas2RoleMsg',
    'org.zstack.core.config.APIQueryGlobalConfigMsg',
    'org.zstack.core.config.APIGetGlobalConfigMsg',
    'org.zstack.core.config.APIUpdateGlobalConfigMsg',
    'org.zstack.header.query.APIGenerateInventoryQueryDetailsMsg',
    'org.zstack.header.query.APIGenerateQueryableFieldsMsg',
    'org.zstack.header.allocator.APIGetHostAllocatorStrategiesMsg',
    'org.zstack.header.allocator.APIGetCpuMemoryCapacityMsg',
    'org.zstack.header.vm.APIMigrateVmMsg',
    'org.zstack.header.vm.APIStopVmInstanceMsg',
    'org.zstack.header.vm.APIGetVmAttachableDataVolumeMsg',
    'org.zstack.header.vm.APIQueryVmNicMsg',
    'org.zstack.header.vm.APIDestroyVmInstanceMsg',
    'org.zstack.header.vm.APIGetVmMigrationCandidateHostsMsg',
    'org.zstack.header.vm.APIQueryVmInstanceMsg',
    'org.zstack.header.vm.APIAttachNicToVmMsg',
    'org.zstack.header.vm.APIRebootVmInstanceMsg',
    'org.zstack.header.vm.APICreateVmInstanceMsg',
    'org.zstack.header.vm.APIStartVmInstanceMsg',
    'org.zstack.header.image.APIChangeImageStateMsg',
    'org.zstack.header.image.APIDeleteImageMsg',
    'org.zstack.header.image.APICreateDataVolumeTemplateFromVolumeMsg',
    'org.zstack.header.image.APICreateRootVolumeTemplateFromRootVolumeMsg',
    'org.zstack.header.image.APIQueryImageMsg',
    'org.zstack.header.image.APICreateRootVolumeTemplateFromVolumeSnapshotMsg',
    'org.zstack.header.image.APIAddImageMsg',
    'org.zstack.header.console.APIRequestConsoleAccessMsg',
    'org.zstack.header.volume.APIBackupDataVolumeMsg',
    'org.zstack.header.volume.APIAttachDataVolumeToVmMsg',
    'org.zstack.header.volume.APIQueryVolumeMsg',
    'org.zstack.header.volume.APICreateDataVolumeFromVolumeSnapshotMsg',
    'org.zstack.header.volume.APICreateDataVolumeFromVolumeTemplateMsg',
    'org.zstack.header.volume.APIDetachDataVolumeFromVmMsg',
    'org.zstack.header.volume.APICreateDataVolumeMsg',
    'org.zstack.header.volume.APIGetDataVolumeAttachableVmMsg',
    'org.zstack.header.volume.APIGetVolumeFormatMsg',
    'org.zstack.header.volume.APIDeleteDataVolumeMsg',
    'org.zstack.header.volume.APICreateVolumeSnapshotMsg',
    'org.zstack.header.volume.APIChangeVolumeStateMsg',
    'org.zstack.header.apimediator.APIIsReadyToGoMsg',
    'org.zstack.header.configuration.APIGenerateApiTypeScriptDefinitionMsg',
    'org.zstack.header.configuration.APIDeleteDiskOfferingMsg',
    'org.zstack.header.configuration.APIGenerateGroovyClassMsg',
    'org.zstack.header.configuration.APIQueryInstanceOfferingMsg',
    'org.zstack.header.configuration.APICreateInstanceOfferingMsg',
    'org.zstack.header.configuration.APIGenerateApiJsonTemplateMsg',
    'org.zstack.header.configuration.APICreateDiskOfferingMsg',
    'org.zstack.header.configuration.APIDeleteInstanceOfferingMsg',
    'org.zstack.header.configuration.APIGenerateSqlVOViewMsg',
    'org.zstack.header.configuration.APIGenerateTestLinkDocumentMsg',
    'org.zstack.header.configuration.APIChangeInstanceOfferingStateMsg',
    'org.zstack.header.configuration.APIGenerateSqlIndexMsg',
    'org.zstack.header.configuration.APIQueryDiskOfferingMsg',
    'org.zstack.header.configuration.APIGenerateSqlForeignKeyMsg',
    'org.zstack.header.configuration.APIChangeDiskOfferingStateMsg',
    'org.zstack.header.storage.primary.APIGetPrimaryStorageTypesMsg',
    'org.zstack.header.storage.primary.APIAttachPrimaryStorageToClusterMsg',
    'org.zstack.header.storage.primary.APIGetPrimaryStorageCapacityMsg',
    'org.zstack.header.storage.primary.APIQueryPrimaryStorageMsg',
    'org.zstack.header.storage.primary.APIChangePrimaryStorageStateMsg',
    'org.zstack.header.storage.primary.APIDeletePrimaryStorageMsg',
    'org.zstack.header.storage.primary.APIReconnectPrimaryStorageMsg',
    'org.zstack.header.storage.primary.APIDetachPrimaryStorageFromClusterMsg',
    'org.zstack.header.storage.primary.APIGetPrimaryStorageAllocatorStrategiesMsg',
    'org.zstack.header.storage.snapshot.APIQueryVolumeSnapshotTreeMsg',
    'org.zstack.header.storage.snapshot.APIDeleteVolumeSnapshotMsg',
    'org.zstack.header.storage.snapshot.APIDeleteVolumeSnapshotFromBackupStorageMsg',
    'org.zstack.header.storage.snapshot.APIQueryVolumeSnapshotMsg',
    'org.zstack.header.storage.snapshot.APIRevertVolumeFromSnapshotMsg',
    'org.zstack.header.storage.snapshot.APIBackupVolumeSnapshotMsg',
    'org.zstack.header.storage.snapshot.APIGetVolumeSnapshotTreeMsg',
    'org.zstack.header.storage.backup.APIQueryBackupStorageMsg',
    'org.zstack.header.storage.backup.APIAttachBackupStorageToZoneMsg',
    'org.zstack.header.storage.backup.APIGetBackupStorageTypesMsg',
    'org.zstack.header.storage.backup.APIChangeBackupStorageStateMsg',
    'org.zstack.header.storage.backup.APIScanBackupStorageMsg',
    'org.zstack.header.storage.backup.APIGetBackupStorageCapacityMsg',
    'org.zstack.header.storage.backup.APIDetachBackupStorageFromZoneMsg',
    'org.zstack.header.storage.backup.APIDeleteBackupStorageMsg',
    'org.zstack.header.network.l3.APIAddDnsToL3NetworkMsg',
    'org.zstack.header.network.l3.APICreateL3NetworkMsg',
    'org.zstack.header.network.l3.APIDeleteIpRangeMsg',
    'org.zstack.header.network.l3.APIChangeL3NetworkStateMsg',
    'org.zstack.header.network.l3.APIAddIpRangeMsg',
    'org.zstack.header.network.l3.APIGetL3NetworkTypesMsg',
    'org.zstack.header.network.l3.APIAddIpRangeByNetworkCidrMsg',
    'org.zstack.header.network.l3.APIQueryIpRangeMsg',
    'org.zstack.header.network.l3.APIRemoveDnsFromL3NetworkMsg',
    'org.zstack.header.network.l3.APIGetIpAddressCapacityMsg',
    'org.zstack.header.network.l3.APIDeleteL3NetworkMsg',
    'org.zstack.header.network.l3.APIQueryL3NetworkMsg',
    'org.zstack.header.network.service.APIAttachNetworkServiceToL3NetworkMsg',
    'org.zstack.header.network.service.APIAddNetworkServiceProviderMsg',
    'org.zstack.header.network.service.APIQueryNetworkServiceL3NetworkRefMsg',
    'org.zstack.header.network.service.APIAttachNetworkServiceProviderToL2NetworkMsg',
    'org.zstack.header.network.service.APIDetachNetworkServiceProviderFromL2NetworkMsg',
    'org.zstack.header.network.service.APIQueryNetworkServiceProviderMsg',
    'org.zstack.header.network.service.APIGetNetworkServiceTypesMsg',
    'org.zstack.header.network.l2.APIAttachL2NetworkToClusterMsg',
    'org.zstack.header.network.l2.APIQueryL2VlanNetworkMsg',
    'org.zstack.header.network.l2.APICreateL2VlanNetworkMsg',
    'org.zstack.header.network.l2.APIDetachL2NetworkFromClusterMsg',
    'org.zstack.header.network.l2.APIDeleteL2NetworkMsg',
    'org.zstack.header.network.l2.APICreateL2NoVlanNetworkMsg',
    'org.zstack.header.network.l2.APIGetL2NetworkTypesMsg',
    'org.zstack.header.network.l2.APIQueryL2NetworkMsg',
    'org.zstack.header.search.APIDeleteSearchIndexMsg',
    'org.zstack.header.search.APISearchGenerateSqlTriggerMsg',
    'org.zstack.header.search.APICreateSearchIndexMsg',
    'org.zstack.header.tag.APIQueryUserTagMsg',
    'org.zstack.header.tag.APIQuerySystemTagMsg',
    'org.zstack.header.tag.APIDeleteTagMsg',
    'org.zstack.header.tag.APICreateUserTagMsg',
    'org.zstack.header.tag.APICreateSystemTagMsg',
    'org.zstack.header.tag.APIQueryTagMsg',
    'org.zstack.header.managementnode.APIQueryManagementNodeMsg',
    'org.zstack.header.message.APICreateMessage',
    'org.zstack.header.cluster.APIQueryClusterMsg',
    'org.zstack.header.cluster.APIDeleteClusterMsg',
    'org.zstack.header.cluster.APICreateClusterMsg',
    'org.zstack.header.cluster.APIChangeClusterStateMsg',
    'org.zstack.header.identity.APIAttachPolicyToUserGroupMsg',
    'org.zstack.header.identity.APIAttachPolicyToUserMsg',
    'org.zstack.header.identity.APICreateAccountMsg',
    'org.zstack.header.identity.APICreateUserGroupMsg',
    'org.zstack.header.identity.APICreateUserMsg',
    'org.zstack.header.identity.APILogInByUserMsg',
    'org.zstack.header.identity.APISessionMessage',
    'org.zstack.header.identity.APIAttachUserToUserGroupMsg',
    'org.zstack.header.identity.APIResetAccountPasswordMsg',
    'org.zstack.header.identity.APILogInByAccountMsg',
    'org.zstack.header.identity.APIValidateSessionMsg',
    'org.zstack.header.identity.APILogOutMsg',
    'org.zstack.header.identity.APICreatePolicyMsg',
    'org.zstack.header.zone.APIDeleteZoneMsg',
    'org.zstack.header.zone.APICreateZoneMsg',
    'org.zstack.header.zone.APIQueryZoneMsg',
    'org.zstack.header.zone.APIChangeZoneStateMsg',
    'org.zstack.header.host.APIChangeHostStateMsg',
    'org.zstack.header.host.APIReconnectHostMsg',
    'org.zstack.header.host.APIDeleteHostMsg',
    'org.zstack.header.host.APIGetHypervisorTypesMsg',
    'org.zstack.header.host.APIQueryHostMsg',
    'org.zstack.header.simulator.APIAddSimulatorHostMsg',
    'org.zstack.header.simulator.storage.primary.APIAddSimulatorPrimaryStorageMsg',
    'org.zstack.header.simulator.storage.backup.APIAddSimulatorBackupStorageMsg',
    'org.zstack.appliancevm.APIQueryApplianceVmMsg',
    'org.zstack.storage.primary.iscsi.APIAddIscsiFileSystemBackendPrimaryStorageMsg',
    'org.zstack.kvm.APIAddKVMHostMsg',
    'org.zstack.storage.primary.nfs.APIAddNfsPrimaryStorageMsg',
    'org.zstack.storage.backup.sftp.APIQuerySftpBackupStorageMsg',
    'org.zstack.storage.backup.sftp.APIReconnectSftpBackupStorageMsg',
    'org.zstack.storage.backup.sftp.APIAddSftpBackupStorageMsg',
    'org.zstack.network.service.virtualrouter.APIReconnectVirtualRouterMsg',
    'org.zstack.network.service.virtualrouter.APICreateVirtualRouterVmMsg',
    'org.zstack.network.service.virtualrouter.APIQueryVirtualRouterOfferingMsg',
    'org.zstack.network.service.virtualrouter.APICreateVirtualRouterOfferingMsg',
    'org.zstack.network.service.virtualrouter.APIQueryVirtualRouterVmMsg',
    'org.zstack.network.service.portforwarding.APIAttachPortForwardingRuleMsg',
    'org.zstack.network.service.portforwarding.APIDetachPortForwardingRuleMsg',
    'org.zstack.network.service.portforwarding.APIGetPortForwardingAttachableVmNicsMsg',
    'org.zstack.network.service.portforwarding.APIChangePortForwardingRuleStateMsg',
    'org.zstack.network.service.portforwarding.APICreatePortForwardingRuleMsg',
    'org.zstack.network.service.portforwarding.APIQueryPortForwardingRuleMsg',
    'org.zstack.network.service.portforwarding.APIDeletePortForwardingRuleMsg',
    'org.zstack.network.service.eip.APIDetachEipMsg',
    'org.zstack.network.service.eip.APIGetEipAttachableVmNicsMsg',
    'org.zstack.network.service.eip.APIQueryEipMsg',
    'org.zstack.network.service.eip.APIChangeEipStateMsg',
    'org.zstack.network.service.eip.APIDeleteEipMsg',
    'org.zstack.network.service.eip.APICreateEipMsg',
    'org.zstack.network.service.eip.APIAttachEipMsg',
    'org.zstack.network.securitygroup.APIChangeSecurityGroupStateMsg',
    'org.zstack.network.securitygroup.APIDetachSecurityGroupFromL3NetworkMsg',
    'org.zstack.network.securitygroup.APIDeleteSecurityGroupRuleMsg',
    'org.zstack.network.securitygroup.APICreateSecurityGroupMsg',
    'org.zstack.network.securitygroup.APIQueryVmNicInSecurityGroupMsg',
    'org.zstack.network.securitygroup.APIQuerySecurityGroupMsg',
    'org.zstack.network.securitygroup.APIAddSecurityGroupRuleMsg',
    'org.zstack.network.securitygroup.APIQuerySecurityGroupRuleMsg',
    'org.zstack.network.securitygroup.APIDeleteSecurityGroupMsg',
    'org.zstack.network.securitygroup.APIDeleteVmNicFromSecurityGroupMsg',
    'org.zstack.network.securitygroup.APIGetCandidateVmNicForSecurityGroupMsg',
    'org.zstack.network.securitygroup.APIAttachSecurityGroupToL3NetworkMsg',
    'org.zstack.network.securitygroup.APIAddVmNicToSecurityGroupMsg',
    'org.zstack.network.service.vip.APIDeleteVipMsg',
    'org.zstack.network.service.vip.APIChangeVipStateMsg',
    'org.zstack.network.service.vip.APICreateVipMsg',
    'org.zstack.network.service.vip.APIQueryVipMsg',
]