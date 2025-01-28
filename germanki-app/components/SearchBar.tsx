import React, { useState } from 'react';
import { SearchBar } from '@rneui/themed';
import { View, StyleSheet } from 'react-native';

type SearchBarComponentProps = {};

const RNESearchBar: React.FunctionComponent<SearchBarComponentProps> = () => {
const [search, setSearch] = useState("");

const updateSearch = (search: string) => {
  setSearch(search);
};

return (
  <View style={styles.view}>
    <SearchBar style={styles.searchbar}
      platform='android'
      placeholder="Search"
      onChangeText={updateSearch}
      value={search}
    />
  </View>
);
};

const styles = StyleSheet.create({
  view: {
    width: '100%',
  },
  searchbar: {
    backgroundColor: 'transparent',
  }
});

export default RNESearchBar;