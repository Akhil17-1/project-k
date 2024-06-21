import React from 'react';
import styled from 'styled-components';
import { Link } from 'react-router-dom';

const SidebarContainer = styled.div`
  width: 250px;
  height: 100%;
  background-color: #333;
  color: white;
  position: fixed;
  top: 0;
  left: ${({ isOpen }) => (isOpen ? '0' : '-250px')};
  transition: left 0.3s ease-in-out;
  z-index: 10;
`;

const MenuList = styled.ul`
  list-style-type: none;
  padding: 0;
`;

const MenuItem = styled.li`
  padding: 15px 20px;
  cursor: pointer;

  &:hover {
    background-color: #444;
  }
`;

const Sidebar = ({ isOpen, toggleMenu }) => {
  return (
    <SidebarContainer isOpen={isOpen}>
      <MenuList>
        <MenuItem onClick={toggleMenu}>
          <Link to="/">Home</Link>
        </MenuItem>
        <MenuItem onClick={toggleMenu}>
          <Link to="/verify-file">Verify File</Link>
        </MenuItem>
        <MenuItem onClick={toggleMenu}>About Us</MenuItem>
        <MenuItem onClick={toggleMenu}>Scope</MenuItem>
        <MenuItem onClick={toggleMenu}>Further Developments</MenuItem>
      </MenuList>
    </SidebarContainer>
  );
};

export default Sidebar;
