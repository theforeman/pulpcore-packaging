%global pulpcore_version nightly

%define repo_dir %{_sysconfdir}/yum.repos.d
%define repo_dist %{dist}

%global release 1

Name:           pulpcore-release
Version:        3.73
Release:        %{?prerelease:0.}%{release}%{?prerelease}%{?dist}
Summary:        Definition of yum repositories for Pulp

Group:          Applications/Internet
License:        GPLv2
URL:            https://pulpproject.org/
Source0:        pulpcore-release.repo

BuildArch:      noarch

BuildRequires:  sed

%description
Defines yum repositories for Pulp.

%prep

%build

%install
rm -rf %{buildroot}

#prepare dir structure
install -d -m 0755 %{buildroot}%{repo_dir}
install -d -m 0755 %{buildroot}%{_sysconfdir}/pki/rpm-gpg/

install -m 644 %{SOURCE0} %{buildroot}%{repo_dir}/

if [[ '%{release}' == *"nightly"* ]];then
    REPO_VERSION='nightly'
    REPO_NAME='Nightly'
    REPO_GPGCHECK=0
else
    # Get major.minor from the version
    REPO_VERSION="$(echo '%{version}' | sed 's/\([^\.]\+\.[^\.]\+\)\..\+/\1/')"
    REPO_NAME=$REPO_VERSION
    REPO_GPGCHECK=1
fi

for repofile in %{buildroot}%{repo_dir}/*.repo; do
    trimmed_dist=`echo %{repo_dist} | sed 's/^\.//'`
    sed -i "s/@DIST@/${trimmed_dist}/" $repofile
    sed -i "s/@RHEL@/%{rhel}/" $repofile
    sed -i "s/@REPO_VERSION@/${REPO_VERSION}/" $repofile
    sed -i "s/@REPO_NAME@/${REPO_NAME}/" $repofile
    sed -i "s/@REPO_GPGCHECK@/${REPO_GPGCHECK}/" $repofile
    sed -i "s/@PULPCORE_VERSION@/%pulpcore_version/" $repofile
done

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%config %{repo_dir}/*.repo

%changelog
* Tue Sep 9 2025 Evgeni Golov - 3.73-1
- Release 3.73

* Thu Jun 19 2025 Eric D. Helms <ericdhelms@gmail.com> - 3.73-0.2.nightly
- Bump release to rebuild

* Mon Jun 16 2025 Odilon Sousa <osousa@redhat.com> - 3.73-0.1.nightly
- Initial package
