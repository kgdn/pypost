#!/usr/bin/env python3

# Author: Kieran Gordon
# Date: 13/06/2022
#
# Description: Creates a Jekyll blog post in the current directory.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from datetime import date
import os

date = date.today()


def display_logo():
    print("\n██████╗░██╗░░░██╗██████╗░░█████╗░░██████╗████████╗")
    print("██╔══██╗╚██╗░██╔╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝")
    print("██████╔╝░╚████╔╝░██████╔╝██║░░██║╚█████╗░░░░██║░░░")
    print("██╔═══╝░░░╚██╔╝░░██╔═══╝░██║░░██║░╚═══██╗░░░██║░░░")
    print("██║░░░░░░░░██║░░░██║░░░░░╚█████╔╝██████╔╝░░░██║░░░")
    print("╚═╝░░░░░░░░╚═╝░░░╚═╝░░░░░░╚════╝░╚═════╝░░░░╚═╝░░░\n")
    print("A blog post creator for Jekyll.\n")


def create_file():
    global file_name
    global title
    global description
    global author
    global tags_list

    title = input("Enter title: ")
    if title == "":
        title = "Untitled Blog Post"

    description = input("Enter description: ")
    if description == "":
        description = "No description"

    author = input("Enter author (press enter for default): ")
    if author == "":
        author = "Anonymous"

    tags = input("Enter tag(s) separated by commas: ")
    tags_list = tags.split(",")
    for i in range(len(tags_list)):
        tags_list[i] = tags_list[i].strip()

    file_name = title.replace(" ", "-") + ".md"
    file_name = file_name.lower()


def export_file():
    f = open(date.strftime("%Y-%m-%d") + "-" + file_name, "w")
    f.write("---\n")
    f.write("layout: post\n")
    f.write("title: \"" + title + "\"\n")
    f.write("date: \"" + str(date) + "\"\n")
    f.write("description: \"" + description + "\"\n")
    f.write("author: \"" + author + "\"\n")
    f.write("tags: " + str(tags_list) + "\n")
    f.write("---\n")
    f.close()
    print("Post created!")


def open_editor():
    editor = os.getenv('EDITOR')
    choice = input("Do you want to open the file in your editor? (y/n): ")
    if choice == "y" or choice == "Y":
        os.system(editor + " " + date.strftime("%Y-%m-%d") + "-" + file_name)
    elif choice == "n" or choice == "N":
        print("Exiting...")
    else:
        print("Invalid input. Please try again.")
        open_editor()


def main():
    display_logo()
    create_file()
    export_file()
    open_editor()


if __name__ == "__main__":
    main()
