// components/SearchBar.tsx

import React, { useState } from "react";
import { View, Text, StyleSheet } from "react-native";
import { SearchBar } from "@rneui/themed";

interface SearchBarProps {
  placeholder: string;
}

export const CustomSearchBar: React.FunctionComponent<SearchBarProps> = ({placeholder = 'Search...'}) => {
  const [search, setSearch] = useState('');

  const UpdateSearch = (text: string) => {
    setSearch(text);
  };

  return (
    <View style={styles.container}>
      <SearchBar 
        placeholder={placeholder}
        onChangeText={UpdateSearch}
        value={search}
      />
    </View>
  );
}

const styles = StyleSheet.create(
  {
    container: {
      margin: 10,
    },
  }
);