%global dracutlibdir    %{_prefix}/lib/dracut

# https://github.com/coreos/coreos-installer
%global commit          081d4bed42489a48e95f559022d96f4999e56cbd
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:      coreos-installer
Version:   0
Release:   1.git%{shortcommit}%{?dist}
Summary:   Installer for CoreOS style systems
License:   GPLv3
URL:       https://github.com/coreos/%{name}
Source0:   %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildArch: noarch


# Keep this up to date with the list in module-setup.sh
# https://github.com/coreos/coreos-installer/blob/master/dracut-module/module-setup.sh
Requires:  /usr/bin/chvt
Requires:  /usr/bin/lsblk
Requires:  /usr/bin/tee
Requires:  /usr/bin/gpg2
Requires:  /usr/bin/curl
Requires:  /usr/sbin/wipefs
Requires:  /usr/sbin/blockdev
Requires:  /usr/bin/dd
Requires:  /usr/bin/dialog
Requires:  /usr/bin/dc
Requires:  /usr/bin/awk
Requires:  /usr/bin/pidof
Requires:  /usr/bin/sha256sum
Requires:  /usr/bin/zcat


%description
This package contains the coreos-installer script used to install CoreOS 
disk images to bare metal machines.

%prep
%autosetup -n %{name}-%{commit} -p1

%build

%install
# main package
install -d -p %{buildroot}%{_libexecdir}
install -p -m 0755 ./coreos-installer %{buildroot}%{_libexecdir}
# dracut subpackage
install -d -p %{buildroot}/%{dracutlibdir}/modules.d
cp -r dracut/* %{buildroot}/%{dracutlibdir}/modules.d/


%files
%doc README.md
%license LICENSE
%{_libexecdir}/coreos-installer

############## dracut subpackage ##############
%package dracut

Summary:   Dracut modules for CoreOS Installer
License:   GPLv3
Requires:  %{name} = %{version}-%{release}
Requires:  dracut
Requires:  dracut-network

%description dracut
Dracut module that enables the CoreOS installer to run in the
initramfs on boot.

%files dracut
%doc README.md
%license LICENSE
%{dracutlibdir}/modules.d/30coreos-installer
############## end dracut subpackage ##############

%changelog
* Thu Feb 14 2019 Dusty Mabe <dusty@dustymabe.com> - 0-1.git081d4be
- Initial Commit
