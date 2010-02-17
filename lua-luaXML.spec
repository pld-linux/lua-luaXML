%define luadir	/lua/5.1
Summary:	LuaXML provides a minimal set of functions for the processing of XML data in Lua
Name:		lua-luaXML
Version:	1.7.2
Release:	0.1
License:	BSD-like
Group:		Development/Languages
Source0:	http://www.viremo.de/LuaXML/LuaXML_090910.zip
# Source0-md5:	de690d73a34bdc7d3b4f0307a40afd87
URL:		http://www.viremo.de/LuaXML/
BuildRequires:	lua51-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LuaXML provides a minimal set of functions for the processing of XML
data in Lua.

%prep
%setup -q -c

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} $(pkg-config --cflags lua51)" \
	LIBS="%{rpmldflags} $(pkg-config --libs lua51)"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}%{luadir}
install -d $RPM_BUILD_ROOT%{_libdir}%{luadir}

install LuaXML_lib.so $RPM_BUILD_ROOT%{_libdir}%{luadir}
install LuaXml.lua $RPM_BUILD_ROOT%{_datadir}%{luadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt test.lua test.xml
%{_datadir}%{luadir}/LuaXml.lua
%{_libdir}%{luadir}/LuaXML_lib.so
