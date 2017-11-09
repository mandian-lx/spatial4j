%{?_javapackages_macros:%_javapackages_macros}

Name:          spatial4j
Version:       0.5.0
Release:       6.1
Summary:       A Geospatial Library for Java
License:       ASL 2.0
Group:         Development/Java
URL:           https://github.com/locationtech/spatial4j
Source0:       https://github.com/spatial4j/spatial4j/archive/%{name}-0.5.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.vividsolutions:jts)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.noggit:noggit)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

# test deps
%if 0
BuildRequires: mvn(com.carrotsearch.randomizedtesting:randomizedtesting-runner)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.slf4j:slf4j-simple)
%endif

BuildArch:     noarch

%description
Spatial4j is a general purpose spatial/geospatial Java library.
It's core capabilities are 3-fold: to provide common geospatially-aware shapes,
to provide distance calculations and other math, and to read and write the
shapes to strings.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-0.5

# Unwanted tasks
%pom_remove_plugin de.thetaphi:forbiddenapis
%pom_remove_plugin org.jacoco:jacoco-maven-plugin

# the attach-sources execution breaks OSGi manifest generation
%pom_remove_plugin :maven-jar-plugin

%mvn_file : %{name}

%build

# Test skipped for unavailable test deps
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc CHANGES.md README.md
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun 20 2016 gil cattaneo <puntogil@libero.it> 0.5.0-4
- add missing build requires: maven-plugin-bundle

* Fri Feb 26 2016 Michael Simacek <msimacek@redhat.com> - 0.5.0-3
- Remove jar-plugin execution to fix manifest generation

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Alexander Kurtakov <akurtako@redhat.com> 0.5.0-1
- Update to 0.5 release.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 11 2015 gil cattaneo <puntogil@libero.it> 0.4.1-3
- introduce license macro

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 10 2014 gil cattaneo <puntogil@libero.it> 0.4.1-1
- update to 0.4.1
- switch to java-headless (build)requires (rhbz#1068543)

* Thu Jan 23 2014 gil cattaneo <puntogil@libero.it> 0.4-1
- update to 0.4

* Mon Aug 26 2013 gil cattaneo <puntogil@libero.it> 0.3-1
- initial rpm

