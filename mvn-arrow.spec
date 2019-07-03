#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-arrow
Version  : 0.10.0
Release  : 2
URL      : https://repo1.maven.org/maven2/org/apache/arrow/arrow-memory/0.10.0/arrow-memory-0.10.0.jar
Source0  : https://repo1.maven.org/maven2/org/apache/arrow/arrow-memory/0.10.0/arrow-memory-0.10.0.jar
Source1  : https://repo1.maven.org/maven2/org/apache/arrow/arrow-memory/0.10.0/arrow-memory-0.10.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause MIT NCSA
Requires: mvn-arrow-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-arrow package.
Group: Data

%description data
data components for the mvn-arrow package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/arrow/arrow-memory/0.10.0
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/apache/arrow/arrow-memory/0.10.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/arrow/arrow-memory/0.10.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/arrow/arrow-memory/0.10.0


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/arrow/arrow-memory/0.10.0/arrow-memory-0.10.0.jar
/usr/share/java/.m2/repository/org/apache/arrow/arrow-memory/0.10.0/arrow-memory-0.10.0.pom
