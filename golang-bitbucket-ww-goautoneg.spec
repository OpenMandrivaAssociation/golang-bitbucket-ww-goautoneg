# https://bitbucket.org/ww/goautoneg
%global goipath     bitbucket.org/ww/goautoneg
%global commit      75cd24fc2f2c2a2088577d12123ddee5f54e0675
%global scm         hg

%gometa

Name:           %{goname}
Version:        0
Release:        0.18%{?dist}
Summary:        HTTP Content-Type Autonegotiation
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:	glide.lock
Source2:	glide.yaml
Patch0:         move-license-to-LICENSE.patch

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgesetup
%patch0 -p1
cp %{SOURCE1} %{SOURCE2} .

%install
%goinstall -e .go -e .txt glide.lock glide.yaml

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.txt

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.hg75cd24f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.17.hg75cd24f
- Upload glide.lock and glide.yaml files
  related: #1247619

* Mon Mar 05 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.16.hg75cd24f
- Update to spec 3.0

* Fri Feb 23 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.15.20120707git75cd24fc2f2c
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.git75cd24fc2f2c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.git75cd24fc2f2c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.git75cd24fc2f2c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git75cd24fc2f2c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 17 2016 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.git75cd24fc2f2c
- Polish the spec file
  related: #1247619

* Mon Aug 08 2016 jchaloup <jchaloup@redhat.com> - 0-0.9.git75cd24fc2f2c
- Enable devel and unit-test for epel7
  related: #1247619

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.git75cd24fc2f2c
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.git75cd24fc2f2c
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git75cd24fc2f2c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.git75cd24fc2f2c
- Update to spec-2.1
  resolves: #1247619

* Tue Jul 28 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.git75cd24fc2f2c
- Update of spec file to spec-2.0
  resolves: #1247619

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.git75cd24fc2f2c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 05 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.git75cd24fc2f2c
- Add missing provides
  related: #1198803

* Wed Mar 04 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git75cd24fc2f2c
- First package for Fedora
  resolves: #1198803

