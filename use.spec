#
Summary:	UML-Based Specification Environment
Summary(pl.UTF-8):	Środowisko tworzenia specyfikacji oparte na UML
Name:		use
Version:	2.4.0
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://www.db.informatik.uni-bremen.de/projects/%{name}-%{version}.tar.gz
# Source0-md5:	92e39f0edc6df05b4be15a267847c26e
URL:		http://www.db.informatik.uni-bremen.de/projects/USE/
Requires:	readline
Requires:	java
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
USE is a system for the specification of information systems. It is
based on a subset of the Unified Modeling Language (UML)

%description -l pl.UTF-8
USE jest programem do tworzenia specyfikacji systemów informatycznych.
Jest oparty na podzbiorze UML-a.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/use/{bin,etc,images,lib}
install -d $RPM_BUILD_ROOT%{_bindir}

cp -a etc $RPM_BUILD_ROOT%{_libdir}/use
cp -a images $RPM_BUILD_ROOT%{_libdir}/use
cp -a lib $RPM_BUILD_ROOT%{_libdir}/use
install bin/use	$RPM_BUILD_ROOT%{_libdir}/use/bin
ln -sf %{_libdir}/use/bin/use $RPM_BUILD_ROOT%{_bindir}/use

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README README.OCL doc examples
%attr(755,root,root) %{_bindir}/use
%dir %{_libdir}/use
%dir %{_libdir}/use/bin
%dir %{_libdir}/use/etc
%dir %{_libdir}/use/images
%dir %{_libdir}/use/lib
%attr(755,root,root) %{_libdir}/use/bin/use
%{_libdir}/use/lib/*
%{_libdir}/use/etc/*
%{_libdir}/use/images/*
