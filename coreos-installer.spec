%global dracutlibdir    %{_prefix}/lib/dracut
%global provider        github
%global provider_tld    com
%global project         coreos
%global project         dustymabe
%global repo            coreos-installer
# https://github.com/coreos/coreos-installer
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          a32b8e28f945602d0a6e784e9ba319b225ee9ee2
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:      coreos-installer
Version:   0
Release:   1.git%{shortcommit}%{?dist}
Summary:   Installer for CoreOS style systems
License:   GPLv3
URL:       https://%{provider_prefix}
Source0:   https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

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
This package contains differentiated branding and configuration for Fedora
Atomic for use in a product.img file for Anaconda, the Fedora installer. It
is not useful on an installed system.

%prep
# setup command reference: http://ftp.rpm.org/max-rpm/s1-rpm-inside-macros.html
# unpack source0 and apply patches
%setup -T -b 0 -q -n %{repo}-%{commit}

%build

%install
# main package
install -d -p %{buildroot}%{_libexecdir}
install -p -m 0754 ./coreos-installer %{buildroot}%{_libexecdir}
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
Requires:  coreos-installer
Requires:  dracut
Requires:  dracut-network
BuildArch: noarch

%description dracut
Dracut module that enables the CoreOS Installer to run in the
initramfs on boot.

%files dracut
%doc README.md
%license LICENSE
%{dracutlibdir}/modules.d/30coreos-installer
############## end dracut subpackage ##############

%changelog
* Thu Feb 14 2019 Dusty Mabe <dusty@dustymabe.com> - 0-1
- Initial Commit
